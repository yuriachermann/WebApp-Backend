# Generated by Django 3.1.3 on 2022-07-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atwdm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='processed_image',
            field=models.CharField(default='', max_length=200),
        ),
    ]
