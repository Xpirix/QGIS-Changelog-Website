# Generated by Django 2.2.18 on 2021-12-03 00:56

from django.db import migrations, models


def add_certification_type_as_existing_value(apps, schema_editor):
    CertificateType = apps.get_model('certification', 'CertificateType')
    CertificateType.objects.create(
        name='attendance and completion',
        wording='Has attended and completed the course:',
        order=0
    )


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0006_auto_20210730_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Certificate type.', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, help_text='Certificate type description - 1000 characters limit.', max_length=1000, null=True)),
                ('wording', models.CharField(help_text='Wording that will be placed on certificate. e.g. "Has attended and completed".', max_length=500)),
                ('order', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),

        migrations.RunPython(add_certification_type_as_existing_value, reverse_code=migrations.RunPython.noop),
    ]
