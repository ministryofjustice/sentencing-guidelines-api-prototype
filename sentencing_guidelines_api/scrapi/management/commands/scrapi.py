from django.core.management.base import BaseCommand, CommandError
from ._offences import OffenceScraper
from ....api import models
import pprint

class Command(BaseCommand):
    help = 'Scrapes offences'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        scraper = OffenceScraper()
        offences = scraper.get_offences(5)
        for offence in offences:
            model, _created = models.Offence.objects.update_or_create(offence_name=offence["name"], defaults = {"effective_from": offence["effective_date"]})
            self.stdout.write(self.style.SUCCESS(model))
            pprint.pprint(offence, indent=4)

        self.stdout.write(self.style.SUCCESS('Command has run successfully'))
