# Generated by Django 3.2.4 on 2021-11-30 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorders',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='db_app.customer', unique=True),
        ),
    ]
