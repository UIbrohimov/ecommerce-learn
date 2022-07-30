from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0003_alter_gallery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'kategoriya',
                'verbose_name_plural': 'Rasm kategoriyalari',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='extra.imgcategory'),
        ),
    ]