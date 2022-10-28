# Generated by Django 4.0 on 2022-05-01 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('patient_code', models.CharField(max_length=100, unique=True)),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientUploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='uploads/')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patients')),
            ],
        ),
    ]