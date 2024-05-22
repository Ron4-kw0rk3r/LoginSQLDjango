# Generated by Django 5.0.3 on 2024-05-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portflyCrab', '0003_acceso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dacceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
