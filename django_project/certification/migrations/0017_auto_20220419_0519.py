# Generated by Django 3.2.13 on 2022-04-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0016_auto_20220418_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='certifyingorganisation',
            name='owner_message',
            field=models.TextField(blank=True, help_text='Message from owner of this organisation.', null=True),
        ),
        migrations.AddField(
            model_name='historicalcertifyingorganisation',
            name='owner_message',
            field=models.TextField(blank=True, help_text='Message from owner of this organisation.', null=True),
        ),
    ]
