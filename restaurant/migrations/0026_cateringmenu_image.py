# Generated by Django 4.2.5 on 2024-01-04 20:59

from django.db import migrations, models
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0025_maindetails_catering_menu_text_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cateringmenu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_for_catering),
        ),
    ]
