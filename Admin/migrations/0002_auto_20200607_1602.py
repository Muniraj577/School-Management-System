# Generated by Django 3.0.6 on 2020-06-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='image',
            field=models.ImageField(upload_to='adminUser/images'),
        ),
    ]
