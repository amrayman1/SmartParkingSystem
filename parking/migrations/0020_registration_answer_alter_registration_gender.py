# Generated by Django 4.0.6 on 2022-07-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0019_complaints_mname'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='answer',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
    ]
