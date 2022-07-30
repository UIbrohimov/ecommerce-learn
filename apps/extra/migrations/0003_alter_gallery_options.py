from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0002_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ('id',), 'verbose_name': 'rasm', 'verbose_name_plural': 'Rasmlar'},
        ),
    ]