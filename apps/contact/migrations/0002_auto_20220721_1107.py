# Generated by Django 3.2 on 2022-07-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='Address',
        ),
        migrations.AddField(
            model_name='contact',
            name='email2',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone2',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]