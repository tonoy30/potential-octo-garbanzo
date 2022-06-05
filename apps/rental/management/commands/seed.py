import json
import logging

from apps.rental.models import Product
from django.core.management.base import BaseCommand

# python manage.py seed --mode=refresh

""" Clear all data and creates products """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self.run_seed(options['mode'])
        self.stdout.write('done.')

    def run_seed(self, mode):
        clear_data()
        if mode == MODE_CLEAR:
            return
        create_products()


def clear_data():
    """
        Deletes all the table data
    """
    logging.info("Delete Product instances")
    Product.objects.all().delete()


def create_products():
    """
        Creates a Product object
    """
    logging.info("Creating product")
    with open('seed.json', 'r') as f:
        data = json.load(f)
    for d in data:
        product = Product(code=d['code'], name=d['name'],
                          type=d['type'], availability=d['availability'], needing_repair=d['needing_repair'],
                          durability=d['durability'], max_durability=d['max_durability'], mileage=d['mileage'],
                          price=d['price'], minimum_rent_period=d['minimum_rent_period']
                          )
        product.save()
        logging.info("{} address created.".format(product))
