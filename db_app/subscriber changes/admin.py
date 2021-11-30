from django.contrib import admin
from db_app import models

admin.site.register(models.Item)
admin.site.register(models.Customer)
admin.site.register(models.Subscriber)
admin.site.register(models.SubOnlyItem)
admin.site.register(models.Preorders)
admin.site.register(models.WeeklyAd)
admin.site.register(models.PreordersSubItem)
admin.site.register(models.BuysSubItem)
admin.site.register(models.Buys)
