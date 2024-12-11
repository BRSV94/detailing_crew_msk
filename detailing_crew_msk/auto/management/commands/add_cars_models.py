import json
from django.core.management.base import BaseCommand

from autos.models import AutoBrand, AutoModel

class Command(BaseCommand):
    help = 'Данная команда создает в бд объекты марок и моделей авто.'

    def handle(self, *args, **options):
        with open('autos/cars.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for brand_item in data:
                brand, create = AutoBrand.objects.get_or_create(
                    name=brand_item['name'],
                    popular=brand_item['popular']
                )
                for model in brand_item['models']:
                    AutoModel.objects.get_or_create(
                        brand=brand,
                        name=model['name']
                    )
        print('All car brands and models have been successfully added to the database')
