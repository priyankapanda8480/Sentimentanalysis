from django.contrib import admin

from .models import *
admin.site.register(WeatherData)
admin.site.register(SentimentAnalysis)
