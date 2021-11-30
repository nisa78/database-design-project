from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Customer, Item, Preorders, SubOnlyItem, WeeklyAd, Subscriber, Buys, BuysSubItem, PreordersSubItem
from .forms import CreateUserForm, SubForm, BuysForm, PreorderForm, SubBuysForm, SubPreorderForm
from django.contrib import messages
import datetime

def home(request):
  weekly_ads = WeeklyAd.objects.raw('SELECT * from db_app_weeklyad')
  return render(request, 'db_project/home.html', {"weekly_ads": weekly_ads})

def substore(request):
  if request.user.is_authenticated:
    if request.user.is_superuser:
      return redirect('db_project-registration')
    try:
      if Subscriber.objects.get(User = Customer.objects.get(User = request.user)):
        substore_list = SubOnlyItem.objects.raw('SELECT * FROM db_app_subonlyitem')
        print('test')
        if request.method == 'POST':
          buysform = SubBuysForm(request.POST)
          preordersform = SubPreorderForm(request.POST)
          print('test')
          if buysform.is_valid():
            buy_item = buysform.cleaned_data.get('buy')
            try:
              BuysSubItem.objects.create(User = Subscriber.objects.get(User = Customer.objects.get(User = request.user)), Item = buy_item)
              messages.success(request, f'Successfully bought {buy_item}!')
            except:
              messages.error(request, f'Already bought {buy_item} before. Cannot buy again.')
          if preordersform.is_valid():
            preorder_item = preordersform.cleaned_data.get('preorder')
            try:
              PreordersSubItem.objects.create(User = Subscriber.objects.get(User = Customer.objects.get(User = request.user)), Item = preorder_item)
              messages.success(request, f'Successfully preordered {preorder_item}!')
            except:
              messages.error(request, f'Already preordered {preorder_item} before. Cannot preorder again.')
        else:
          buysform = BuysForm()
          preordersform = PreorderForm()
        return render(request, 'db_project/substore.html', {'store_list': substore_list, 'buysform': buysform, 'preordersform': preordersform})
      else:
        # Logged in but not subscribed, send to make a new account
        return redirect('db_project-registration')
    except:
      return redirect('db_project-registration')
  else:
    # Not logged in
    return redirect('login')

def store(request):
  store_list = Item.objects.raw('SELECT SKU FROM db_app_item EXCEPT SELECT * FROM db_app_subonlyitem')
  if request.user.is_authenticated:
    if request.method == 'POST':
      buysform = BuysForm(request.POST)
      preordersform = PreorderForm(request.POST)
      if buysform.is_valid():
        buy_item = buysform.cleaned_data.get('buy')
        try:
          Buys.objects.create(User = Customer.objects.get(User = request.user), Item = buy_item)
          messages.success(request, f'Successfully bought {buy_item.Name}!')
        except:
          messages.error(request, f'Already bought {buy_item} before. Cannot buy again.')
      if preordersform.is_valid():
        preorder_item = preordersform.cleaned_data.get('preorder')
        try:
          Preorders.objects.create(User = Customer.objects.get(User = request.user), Item = preorder_item)
          messages.success(request, f'Successfully preordered {preorder_item.Name}!')
        except:
          messages.error(request, f'Already preordered {preorder_item} before. Cannot preorder again.')
    else:
      buysform = BuysForm()
      preordersform = PreorderForm()
    return render(request, 'db_project/store.html', {'store_list': store_list, 'buysform': buysform, 'preordersform': preordersform})
  else: 
    return render(request, 'db_project/store.html', {'store_list': store_list})

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

