# Generated by Django 2.0.6 on 2018-08-30 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExceptionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256)),
                ('message', models.TextField(blank=True, null=True)),
                ('html_message', models.TextField(blank=True, null=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
