# Generated by Django 4.0 on 2022-03-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('flat', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
    ]