# Generated by Django 2.2.18 on 2021-11-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0006_auto_20210730_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseconvener',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Inactive Convener will not be available in your organisation list.'),
        ),
    ]
