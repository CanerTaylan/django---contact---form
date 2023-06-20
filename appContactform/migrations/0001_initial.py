# Generated by Django 4.1.7 on 2023-06-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='isim')),
                ('subject', models.CharField(max_length=50, verbose_name='Konu başlığı')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('message', models.TextField(max_length=550, verbose_name='Mesaj')),
            ],
            options={
                'verbose_name': 'İletişim Formu Mesajı',
                'verbose_name_plural': 'İletişim Formu Mesajları',
            },
        ),
    ]