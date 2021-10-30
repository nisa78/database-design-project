from django.db import models
from datetime import date

<<<<<<< HEAD

class Item(models.Model):
	SKU = models.IntegerField()
	Price = models.IntegerField()
	Discount = models.IntegerField()

class Customer(models.Model):
	UserID = models.IntegerField()
	DOB = models.DateField()
	views = models.TextField()

class Subscriber(models.Model):
	UserID = models.IntegerField()
	SubscriptionDate = models.DateField()

class SubOnlyItem(models.Model):
	SKU = models.IntegerField()

class WeeklyAd(models.Model):
	AdID = models.IntegerField()
	Week = models.DateField()
	Content = models.TextField()
	Lists = models.TextField()

class PreordersSubItem(models.Model):
	UserID = models.IntegerField()
	SKU = models.IntegerField()

class BuysSubItem(models.Model):
	UserID = models.IntegerField()
	SKU = models.IntegerField()

class Buys(models.Model):
	UserID = models.IntegerField()
	SKU = models.IntegerField()



def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
=======
class Item(models.Model):
        SKU = models.IntegerField()
        Price = models.IntegerField()
        Discount = models.IntegerField()

class Customer(models.Model):
        UserID = models.IntegerField()
        DOB = models.DateField()
        views = models.TextField()

class Subscriber(models.Model):
        UserID = models.IntegerField()
        SubscriptionDate = models.DateField()

class SubOnlyItem(models.Model):
    SKU = models.IntegerField()

class WeeklyAd(models.Model):
    AdID = models.IntegerField()
    Week = models.DateField()
    Content = models.TextField()
    Lists = models.TextField()

class PreordersSubItem(models.Model):
    UserID = models.IntegerField()
    SKU = models.IntegerField()

class BuysSubItem(models.Model):
    UserID = models.IntegerField()
    SKU = models.IntegerField()

class Buys(models.Model):
    UserID = models.IntegerField()
    SKU = models.IntegerField()

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
>>>>>>> 606f317ab8ad4ac1d724b3b1410fa70043724c8e
