# Generated by Django 3.0.8 on 2020-07-03 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activityapi', '0002_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tz', timezone_field.fields.TimeZoneField(default='America/Los_Angeles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
