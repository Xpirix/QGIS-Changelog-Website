# Generated by Django 2.2 on 2020-07-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0004_auto_20191204_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingcenter',
            name='address',
            field=models.TextField(help_text='Address of the training center. If your training center is online, you can put your web address of your training center.', max_length=250),
        ),
    ]
