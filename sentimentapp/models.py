# from django.db import models
#
# class WeatherData(models.Model):
#     date = models.DateField()
#     meantemp = models.FloatField()
#
# class Sentimentanalysis(models.Model):
#     text = models.TextField()
#     sentiment_data = models.CharField(max_length = 10)

# myapp/models.py
# models.py

from django.db import models

class SentimentAnalysis(models.Model):
    text = models.TextField()
    sentiment_data = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

class WeatherData(models.Model):
    date = models.DateField()
    weather_data = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
class User(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
