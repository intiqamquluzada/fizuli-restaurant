# Generated by Django 4.2.5 on 2023-09-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Adı')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Əlaqə nömrəsi')),
                ('reserve_date', models.DateTimeField(verbose_name='Rezerv tarixi və saatı')),
                ('count_of_guest', models.IntegerField(verbose_name='Qonaq sayı')),
                ('special_message', models.TextField(verbose_name='Xüsusi istək')),
            ],
            options={
                'verbose_name': 'Rezerv',
                'verbose_name_plural': 'Rezervlər',
                'ordering': ('-created_at',),
            },
        ),
    ]
