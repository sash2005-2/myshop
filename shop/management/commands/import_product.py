import csv

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

        check_goods = False
        file = open('myshop.csv', 'r')
        product = Product.objects.all()
        for line in file:
            arr = line.split(';')
            for p in product:
                print(p.name)
                if arr[0] == p.name:
                    print('Совпало')
                    check_goods = True
            if not check_goods:
                print('check')
                creator(arr[9])
            check_goods = False
            #print(arr[1])
        #file.close()


        self.stdout.write('Successfully')



def creator(category_name):
    category = Category.objects.all()
    for c in category:
        print(c.name)
        print(category_name)
        if c.name == category_name:
            print( c.name)
            print('Мониторы+Тв')
            print('from for category ravno')
        else:
            print(c.name)
            print(category_name)
            print('from for category ne ravno')
    #    category.name = 'Электровеники'
    #    category.slug = 'myvenik'
    #    category.save()
#
    #product = Product()
    #product.name = 'test1'
    #product.slug = 'mytest'
    #product.price = 100
    #product.stock = 12
    #product.available = True
    #product.category = category
    #product.save()
    #self.stdout.write('From creator')


            # Пример как создаётся (сохраняется) категория
            # category = Category()
            # category.name = 'Электровеники'
            # category.slug = 'myvenik'
            # category.save()
            #
            ## и товар
            # product = Product()
            # product.name = 'test1'
            # product.slug = 'mytest'
            # product.price = 100
            # product.stock = 12
            # product.available = True
            # product.category = category
            # product.save()