from django.shortcuts import render
from django.http import HttpResponse
from db_app import models

def home(request):
  weekly_ads = models.WeeklyAd.objects.all()
  return render(request, 'db_project/home.html', {"weekly_ads": weekly_ads})
def about(request):
  return render(request, 'db_project/about.html')
