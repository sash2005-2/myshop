from django.core.management.base import BaseCommand
from shop.models import Product, Category


class Command(BaseCommand):
    help = 'Import products from csv'

    def handle(self, *args, **options):
        """
        Здесь надо реализовать следующее:
        - открываем csv файл
        - читаем из него построчно
        - создаем товары

        Только есть нюанс, категория в данный момент является обязательной
        поэтому тут или в csv файле в каждой строке писать категорию к которой относится товар
        а при загрузке проверять что такая категория есть? если есть то брать существующую, если нет - создавать

        :param args:
        :param options:
        :return:
        """

        # Пример как создаётся (сохраняется) категория
        category = Category()
        category.name = 'Электровеники'
        category.slug = 'myvenik'
        category.save()

        # и товар
        product = Product()
        product.name = 'test1'
        product.slug = 'mytest'
        product.price = 100
        product.stock = 12
        product.available = True
        product.category = category
        product.save()

        self.stdout.write('Successfully')
