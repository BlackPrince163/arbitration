from django.core.management import BaseCommand
from api.services import load_file


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_file.run()