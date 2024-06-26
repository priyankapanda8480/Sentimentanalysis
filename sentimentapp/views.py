from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SentimentForm, WeatherForm
from .models import SentimentAnalysis, WeatherData
import pandas as pd
from django.utils import timezone
import os
import pickle
from django.contrib.auth.models import User
import requests
from huggingface_hub import InferenceClient
import json
# Initialize the Hugging Face Inference Client
hf_api_token = "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"
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm_client = InferenceClient(model=repo_id, token=hf_api_token, timeout=600)

def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},
            "task": "sentiment-analysis",
        },
    )
    return json.loads(response.decode())[0]["generated_text"]

class SentimentAnalysisChain:
    def __init__(self, inference_client, task="text-generation"):
        self.inference_client = inference_client
        self.task = task

    def run(self, input_text):

        prompt = f"Analyze the sentiment of the following text and return whether it is Positive or Negative:\n\n{input_text}"
        response_text = call_llm(self.inference_client, prompt)
        print("Raw response:", response_text)
        sentiment_label = self.extract_sentiment(response_text)
        print(f"Extracted sentiment: {sentiment_label}")

        return sentiment_label

    def extract_sentiment(self, response_text):
        response_lines = response_text.strip().split("\n")
        sentiment_label = "Unknown"
        for line in response_lines[::-1]:
            line = line.strip().lower()
            if "positive" in line:
                sentiment_label = "Positive"
                break
            elif "negative" in line:
                sentiment_label = "Negative"
                break
        return sentiment_label

# Initialize the sentiment analysis chain with llm_client
sentiment_chain = SentimentAnalysisChain(llm_client)

def perform_sentiment_analysis(text):
    return sentiment_chain.run(text)

def predict_sentiment(request):
    selected_model = request.POST.get('model', 'sentiment')
    sentiment_form = SentimentForm()
    weather_form = WeatherForm()
    result = None

    if request.method == 'POST':
        if selected_model == 'sentiment':
            sentiment_form = SentimentForm(request.POST)
            if sentiment_form.is_valid():
                text = sentiment_form.cleaned_data['text']
                sentiment_result = perform_sentiment_analysis(text)
                SentimentAnalysis.objects.create(text=text, sentiment_data=sentiment_result)
                result = sentiment_result
                print(f"Sentiment result: {result}")

            # return redirect('index')

        elif selected_model == 'weather':
            weather_form = WeatherForm(request.POST)
            if weather_form.is_valid():
                date = weather_form.cleaned_data['date']
                weather_result = perform_weather_forecast(date)
                WeatherData.objects.create(date=date, weather_data=weather_result, date_created=timezone.now())
                result = weather_result
                print(f"Weather result: {result}")

    return render(request, 'index.html', {
        'sentiment_form': sentiment_form,
        'weather_form': weather_form,
        'result': result,
        'selected_model': selected_model,
    })

# def perform_sentiment_analysis(text):
#     model_path = os.path.join(os.path.dirname(__file__), 'trained_model.sav')
#     vector_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')
#     with open(model_path, 'rb') as file:
#         model = pickle.load(file)
#     with open(vector_path, 'rb') as file:
#         vectorizer = pickle.load(file)
#     text_vector = vectorizer.transform([text])
#     prediction = model.predict(text_vector)
#     return "Positive" if prediction[0] == 1 else "Negative"


def perform_weather_forecast(date_str):
    model_path = os.path.join(os.path.dirname(__file__), 'linear_regression_model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    date = pd.to_datetime(date_str)
    date_ordinal = date.toordinal()
    features = pd.DataFrame([[date_ordinal]], columns=['date_ordinal'])
    prediction = model.predict(features)
    return prediction[0] if prediction else 0.0

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to your home page
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # You can add validation or other checks here before creating the user
        user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user)
        return redirect('login')  # Redirect to your home page
    return render(request, 'signup.html')
def logout_view(request):
    logout(request)
    return redirect('login')
