from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='carusel/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Carusel',
                'verbose_name_plural': 'Carusel',
            },
        ),
    ]