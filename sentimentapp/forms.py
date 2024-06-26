from django import forms
from django.contrib.auth.models import User

class SentimentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Enter text for sentiment analysis')

class WeatherForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Enter date for weather forecast')
class UserCreationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'eamil'}), label='Enter Email address')
    password = forms.CharField(widget=forms.Textarea,  label='Enter Password')
