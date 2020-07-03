from random import randint
import datetime
import pytz

from django.core.management.base import BaseCommand, CommandError
from activityapi.models import Member, ActivityPeriod
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with dummy data.'

    def handle(self, *args, **options):
        for member in Member.objects.all():
            dummy_size = randint(1, 5)
            for _ in range(dummy_size):
                try:
                    start_time = datetime.datetime.now(pytz.timezone(str(member.tz))) - datetime.timedelta(seconds=randint(1, 86400*365))
                    timediff =  datetime.datetime.now(pytz.timezone(str(member.tz))) - start_time
                    activity = ActivityPeriod(member=member, 
                        start_time = start_time, 
                        end_time=start_time + datetime.timedelta(seconds=randint(1, timediff.seconds)))
                    activity.save()
                except pytz.exceptions.UnknownTimeZoneError:
                    raise CommandError('Unknown Timezone %s of the user.' % str(member.tz))

            self.stdout.write(self.style.SUCCESS('Successfully Populated Data %d entries for %s user.' % (dummy_size, member)))
                
            member.save()

            