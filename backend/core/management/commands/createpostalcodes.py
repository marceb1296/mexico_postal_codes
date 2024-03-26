from django.core.management.base import BaseCommand, CommandError

from core.handler import PostalCodeHandler


class Command(BaseCommand):
    help = "Download, parse and save Postal Codes data"

    def handle(self, *args, **options):

        PostalCodeHandler().manage()
        self.stdout.write("Postal Code data saved correctly")
