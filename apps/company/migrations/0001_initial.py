# Generated by Django 3.2 on 2022-08-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('content', models.TextField(verbose_name='Asosiy qism')),
            ],
            options={
                'verbose_name': 'content',
                'verbose_name_plural': 'contents',
            },
        ),
    ]
