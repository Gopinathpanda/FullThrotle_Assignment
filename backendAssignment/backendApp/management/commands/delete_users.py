from django.core.management.base import BaseCommand
from backendApp.models import User, ActivityPeriods


class Command(BaseCommand):
    help = 'Delete User'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='user Id')

    def handle(self, *args, **kwargs):
        uids = kwargs['id']
        for id in uids:
            try:
                user = User.objects.get(id=id)
                user.delete()
                self.stdout.write(self.style.SUCCESS('User {} deleted with success!'.format(id)))
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING('User {} does not able to delete!'.format(id)))
