from django.core.management.base import BaseCommand
from backendApp.models import User, ActivityPeriods
import random
from datetime import datetime, timedelta
import string
import pytz

uid_list = []
all_users = User.objects.all()
for a in all_users:
    uid_list.append(a.id)


def generate_id():
    n = 10
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return res


def get_member():
    mid = random.randint(1, 100)
    return mid


def generate_date():
    year = random.randint(2000, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 12)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    return datetime(year, month, day, hour, minute, second)


def generate_ok():
    ok = 1
    return ok


def generate_tz():
    a = list(pytz.all_timezones)
    zones = random.randint(0, 592)
    return a[zones]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The Txt file contains user names')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                uid = generate_id()
                uid_list.append(uid)
                user = row
                start_time = generate_date()
                print(start_time)
                rand_hour = random.randint(1, 12)
                end_time = start_time + timedelta(hours=rand_hour)
                timezone = generate_tz()
                print(uid, uid_list, user)

                User.objects.get_or_create(
                    id=uid,
                    real_name=user,
                    tz=timezone,

                )

                ActivityPeriods.objects.get_or_create(
                    start_time=start_time,
                    end_time=end_time,
                    user=User.objects.get(id=uid_list[random.randint(0, len(uid_list) - 1)])
                )

        self.stdout.write(self.style.SUCCESS('User Populate Successfully'))
