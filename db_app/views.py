from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, SubOnlyItem, WeeklyAd
from .forms import CreateUserForm
from django.contrib import messages

def home(request):
  weekly_ads = WeeklyAd.objects.raw('SELECT * from db_app_weeklyad')
  return render(request, 'db_project/home.html', {"weekly_ads": weekly_ads})

def substore(request):
  substore_list = SubOnlyItem.objects.raw('SELECT * FROM db_app_subonlyitem')
  return render(request, 'db_project/substore.html', {'store_list': substore_list})

def store(request):
  store_list = Item.objects.raw('SELECT SKU FROM db_app_item EXCEPT SELECT * FROM db_app_subonlyitem')
  return render(request, 'db_project/store.html',
	{'store_list': store_list})

def registration(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Successfully created account for {username}!')
      return redirect('login')
  else:
    form = CreateUserForm()
  return render(request, 'db_project/registration.html', {'form': form})

