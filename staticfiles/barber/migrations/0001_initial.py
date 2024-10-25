# Generated by Django 5.1 on 2024-10-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('Beauty & spa', 'Beauty & spa'), ('Body massage', 'Body massage'), ('Shaving & Facial', 'Shaving & Facial'), ('Hair Color', 'Hair Color')], default='Beauty & spa', max_length=50)),
                ('date', models.DateField()),
                ('message', models.TextField()),
            ],
        ),
    ]
