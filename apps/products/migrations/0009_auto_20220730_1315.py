# Generated by Django 3.2 on 2022-07-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220730_0510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='result',
            name='content',
            field=models.TextField(verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='result',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255, verbose_name='Product'), max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Product'),
        ),
    ]