# Generated by Django 4.1.1 on 2023-01-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='unkown', max_length=200, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='unkown', max_length=200, verbose_name='last name'),
        ),
    ]
