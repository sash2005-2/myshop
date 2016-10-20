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



        print('Начало модуля**************************************************')
        count = 0
        product = Product.objects.all()
        f = open('newshop.txt')
        for line in f.readlines():
            count += 1
            print(count)
            check_goods = False
            arr = line.strip().split(';')
            if len(arr[4]) > 200:
                arr[4] = arr[4][0:200]
            if len(arr[4]) > 100:
                arr[4] = arr[4][0:100]
            arr[1] = int(arr[1])
            arr[3] = int(arr[3])
            for prod in product:
                if arr[1] == prod.articul:#если продукт с таким артикулом найден, то меняем цену
                    prod.price = arr[3]
                    prod.save()
                    check_goods = True
                    print("Change price")

            if not check_goods:
                check_goods = True
                create_category(arr)
                print('Add goods')

        f.close()
        print('Finished successfull')




def create_category(myarr):
    check_cat = False
    category = Category.objects.all()
    #if len(category) == 0:
    #    create_cat(myarr)

    for cat in category:
        if myarr[4] == cat.name and not check_cat:
            check_cat = True
            create_prod(myarr, cat)
            #myarr[2] = cat.name

    if not check_cat:
            check_cat = True
            create_cat(myarr)


def create_cat(myarr_cat):
    category = Category()
    category.name = myarr_cat[0]
    category.slug = myarr_cat[0]#Необходимо провверять slug на дубли
    category.save()
    create_prod(myarr_cat, category)


def create_prod(myarr_pr, categor):
    product = Product()
    product.articul = myarr_pr[1]
    product.name = myarr_pr[4]
    product.category = categor
    product.slug = myarr_pr[4]#Необходимо провверять slug на дубли
    product.description = myarr_pr[2]
    product.stock = 0
    product.price = myarr_pr[3]
    product.available = True
    product.save()