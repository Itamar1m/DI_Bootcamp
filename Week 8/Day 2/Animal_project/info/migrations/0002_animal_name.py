# Generated by Django 3.1.7 on 2021-03-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
