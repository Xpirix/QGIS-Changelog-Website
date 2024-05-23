# Generated by Django 2.2 on 2019-12-17 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0012_2_8'),
        ('changes', '0002_auto_20191216_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorshiplevel',
            name='subscription_plan',
            field=models.ForeignKey(blank=True, help_text='A Stripe subscription plan contains the pricing information', null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Plan'),
        ),
    ]
