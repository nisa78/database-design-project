from django import forms
from django.db.models import query
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Item, SubOnlyItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class SubForm(forms.Form):
  subscribed = forms.BooleanField(required=True)

class BuysForm(forms.Form):
  buy = forms.ModelChoiceField(queryset=Item.objects.all())

class PreorderForm(forms.Form):
  preorder = forms.ModelChoiceField(queryset=Item.objects.all())

class SubBuysForm(forms.Form):
  buy = forms.ModelChoiceField(queryset=SubOnlyItem.objects.all())

class SubPreorderForm(forms.Form):
  preorder = forms.ModelChoiceField(queryset=SubOnlyItem.objects.all())