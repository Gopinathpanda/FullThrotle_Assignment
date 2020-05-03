from django.db import models
import pytz


class User(models.Model):
    TIMEZONE = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(primary_key=True, max_length=10)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30, choices=TIMEZONE)

    def __str__(self):
        return self.real_name


class ActivityPeriods(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, related_name='activity', on_delete=models.CASCADE)
