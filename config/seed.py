import logging

from apps.rental.models import Product
from django.core.management.base import BaseCommand

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self.run_seed(self, options['mode'])
        self.stdout.write('done.')

    def run_seed(self, mode):
        clear_data()
        if mode == MODE_CLEAR:
            return
        for i in range(15):
            create_product()


def clear_data():
    """
        Deletes all the table data
    """
    logging.info("Delete Address instances")
    Product.objects.all().delete()


def create_product(code, name, type, availability, needing_repair, durability, max_durability, price, minimum_rent_period):
    """
        Creates a Product object
    """
    logging.info("Creating product")
    product = Product()
    product.save()
    logging.info("{} address created.".format(product))
    return product
# [{"_id":1,"code":"p1","name":"Air Compressor 12 GAS","type":"plain","availability":true,"needing_repair":false,"durability":3000,"max_durability":3000,"price":"4500.0","minimum_rent_period":1}]
