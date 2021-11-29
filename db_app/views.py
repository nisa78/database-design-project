from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, WeeklyAd

def home(request):
  weekly_ads = WeeklyAd.objects.all()
  return render(request, 'db_project/home.html', {"weekly_ads": weekly_ads})
def about(request):
  return render(request, 'db_project/about.html')
def store(request):
  store_list = Item.objects.all()
  return render(request, 'db_project/store.html',
	{'store_list': store_list})
