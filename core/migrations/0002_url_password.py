# Generated by Django 3.0.8 on 2020-11-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='password',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
