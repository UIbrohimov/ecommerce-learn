# Generated by Django 3.2 on 2022-07-06 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255, verbose_name='Mahsulot nomi')),
                ('narxi', models.CharField(max_length=255, verbose_name='Narxi')),
                ('tavsifi', models.CharField(max_length=255, verbose_name='Tavsifi')),
                ('rasmi', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Rasmi')),
                ('baho', models.IntegerField(max_length=255, verbose_name='Baho')),
                ('naxt', models.BooleanField(verbose_name='Naqt pul')),
                ('karta', models.BooleanField(verbose_name='Karta orqali')),
                ('active', models.BooleanField(verbose_name='Holati')),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Mahsulot turi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
    ]