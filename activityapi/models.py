from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField


class Member(models.Model):
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


class ActivityPeriod(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.member.user.username + " " + str(self.id)



