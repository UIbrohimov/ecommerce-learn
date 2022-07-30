from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='nomi')),
                ('image', models.ImageField(upload_to='images/', verbose_name='rasm')),
            ],
            options={
                'verbose_name': 'rasm',
                'verbose_name_plural': 'Rasmlar',
            },
        ),
    ]