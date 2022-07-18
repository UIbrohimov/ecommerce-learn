# Generated by Django 3.2 on 2022-07-18 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_baho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(verbose_name='Aktiv'),
        ),
        migrations.AlterField(
            model_name='product',
            name='baho',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Baho'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tavsifi',
            field=models.TextField(max_length=255, verbose_name='Tavsifi'),
        ),
    ]