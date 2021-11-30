from django.db import models
from django.conf import settings
from datetime import date
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey


class Item(models.Model):
	Name = models.CharField(max_length=100, default='')
	SKU = models.AutoField(primary_key=True, unique=True, null=False)
	Price = models.DecimalField(max_digits=8, decimal_places=2)
	Discount = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return str(self.Name)

class WeeklyAd(models.Model):
	AdID = models.AutoField(primary_key=True, unique=True, null=False)
	Week = models.DateField()
	Content = models.TextField()
	Lists = models.ForeignKey(to=Item, null=False, on_delete=models.PROTECT)

	def __str__(self):
		return 'Week {} Ad for {}'.format(self.Week, self.Lists)

class Customer(models.Model):
	User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, unique=True, primary_key=True)
	DOB = models.DateField()
	views = models.ForeignKey(to=WeeklyAd, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.User.username)

class Subscriber(models.Model):
	User = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=False, unique=True, primary_key=True)
	SubscriptionDate = models.DateField()

	def __str__(self):
		return str(self.User.User.username)

class SubOnlyItem(models.Model):
	Item = models.ForeignKey(to=Item, on_delete=models.CASCADE, unique=True, null=False, primary_key=True)

	def __str__(self):
		return str(self.Item.Name)

class Preorders(models.Model):
	User = models.ForeignKey(to=Customer, unique=True, null=False, on_delete=models.PROTECT)
	Item = models.ForeignKey(to=Item, unique=True, null=False, on_delete=models.PROTECT)

	class Meta:
		# Django only supports single-column primary keys: 
		# https://stackoverflow.com/questions/16800375/how-can-i-set-two-primary-key-fields-for-my-models-in-django
		# This is the closest we can get to replicating the effect.
		unique_together = (("User", "Item"))

	def __str__(self):
		return '{} preorders: {}'.format(self.User.User.username, self.Item.Name)


class PreordersSubItem(models.Model):
	User = models.ForeignKey(to=Subscriber, unique=True, null=False, on_delete=models.PROTECT)
	Item = models.ForeignKey(to=SubOnlyItem, unique=True, null=False, on_delete=models.PROTECT)

	class Meta:
		unique_together = (("User", "Item"))

	def __str__(self):
		return '{} preorders: {}'.format(self.User.User.User.username, self.Item.Item.Name)

class BuysSubItem(models.Model):
	User = models.ForeignKey(to=Subscriber, unique=True, null=False, on_delete=models.PROTECT)
	Item = models.ForeignKey(to=SubOnlyItem, unique=True, null=False, on_delete=models.PROTECT)

	class Meta:
		unique_together = (("User", "Item"))
	
	def __str__(self):
		return '{} preorders: {}'.format(self.User.User.User.username, self.Item.Item.Name)

class Buys(models.Model):
	User = models.ForeignKey(to=Customer, unique=True, null=False, on_delete=models.PROTECT)
	Item = models.ForeignKey(to=Item, unique=True, null=False, on_delete=models.PROTECT)

	class Meta:
		unique_together = (("User", "Item"))

	def __str__(self):
		return '{} buys: {}'.format(self.User.User.username, self.Item.Name)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
