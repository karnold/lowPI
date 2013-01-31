from django.core.management.base import BaseCommand, CommandError
from air import suspension

class Command(BaseCommand):
    help = 'Testing'
    s = suspension.suspension()

    def handle(self, *args, **options):
        self.s.diagnostic()
