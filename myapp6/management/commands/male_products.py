from random import choice, randint, uniform
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from myapp5.models import Category, Product


class Command(BaseCommand):
    help = 'Generate fake products'


    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Score products for generate')


    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count+1):
            products.append(Product(
                name = f'Product #{i}',
                category = choice(categories),
                description = 'hevbebvewnv erwfnewfnweo ewfnwefnwenf',
                price = uniform(0.01, 999999.99),
                quantity = randint(1, 10000),
                rating = uniform(0.01, 9.99)
            ))
        Product.objects.bulk_create(products)