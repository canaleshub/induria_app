# Generated by Django 4.0 on 2022-05-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientuploads',
            name='predicted_class',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
