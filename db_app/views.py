from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Customer, Item, SubOnlyItem, WeeklyAd, Subscriber
from .forms import CreateUserForm, SubForm
from django.contrib import messages
import datetime

def home(request):
  weekly_ads = WeeklyAd.objects.raw('SELECT * from db_app_weeklyad')
  return render(request, 'db_project/home.html', {"weekly_ads": weekly_ads})

def substore(request):
  if request.user.is_authenticated:
    try:
      # Test if user is not considered a customer (AKA Superusers)
      Customer.objects.get(User = request.user)
    except:
      # Return to registration if not a customer
      return redirect('db_project-registration')
    if Subscriber.objects.get(User = Customer.objects.get(User = request.user)):
      substore_list = SubOnlyItem.objects.raw('SELECT * FROM db_app_subonlyitem')
      return render(request, 'db_project/substore.html', {'store_list': substore_list})
    else:
      # Logged in but not subscribed, send to make a new account
      return redirect('db_project-registration')
  else:
    # Not logged in
    return redirect('login')

def store(request):
  store_list = Item.objects.raw('SELECT SKU FROM db_app_item EXCEPT SELECT * FROM db_app_subonlyitem')
  return render(request, 'db_project/store.html',
	{'store_list': store_list})

def registration(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    subform = SubForm(request.POST)
    if form.is_valid():
      form.save()
      new_username = form.cleaned_data.get('username')
      messages.success(request, f'Successfully created account for {new_username}!')
      Customer.objects.create(User = User.objects.get(username = new_username), DOB = datetime.datetime.now(), views=WeeklyAd.objects.latest('Week'))
      if subform.is_valid():
        Subscriber.objects.create(User = Customer.objects.get(User = User.objects.get(username = new_username)), SubscriptionDate = datetime.datetime.now())
        return redirect('login')
  else:
    form = CreateUserForm()
    subform = SubForm()
  return render(request, 'db_project/registration.html', {'form': form, 'subform': subform})

