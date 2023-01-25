# Generated by Django 4.1.1 on 2023-01-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_remove_restaurant_rating_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(choices=[(1, 'FAST_FOOD'), (2, 'CASUAL_DINING'), (3, 'FAST_CASUAL'), (4, 'CONTEMPORARY'), (5, 'CAFE'), (6, 'PIZZERIA')], default='Casual dining', max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(blank=True, choices=[(1, '$'), (2, '$$'), (3, '$$$')], null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='zip',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]