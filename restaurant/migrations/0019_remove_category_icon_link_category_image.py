# Generated by Django 4.2.5 on 2023-10-07 16:11

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_alter_category_icon_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon_link',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='286x286', null=True, upload_to=services.uploader.Uploader.upload_photo_for_icon, verbose_name='Kateqoriya fotosu'),
        ),
    ]
