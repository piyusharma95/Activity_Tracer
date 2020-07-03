from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField


# Create your models here.
class member(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    tz = TimeZoneField(default='America/Los_Angeles')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

