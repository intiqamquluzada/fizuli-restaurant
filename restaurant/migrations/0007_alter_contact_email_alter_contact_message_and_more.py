# Generated by Django 4.2.5 on 2023-09-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Elektron poçtu'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name_and_surname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adı və soyadı'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Mövzu'),
        ),
    ]
