from typing import re

from django.core.management import BaseCommand
from shop.models import Product, Category
import xlrd, xlwt


class Command(BaseCommand):
    help = 'read xls file'

    def handle(self, *args, **options):


        count = 0
        rb = xlrd.open_workbook('test.xls', formatting_info=True) # открываем файл
        sheet = rb.sheet_by_index(0)# выбираем активный лист


        val = sheet.nrows#задаем переменной количество строк в файле
        for vv in range(val):
            value = sheet.row_values(vv)
            #value[3] = float(str(value[3]).replace(',', '.'))#меняем в цене запятую на точку и преобразуем в строку
            check_prod = False
            products = Product.objects.all()
            for product in products:
                if value[1] == product.articul:
                    print('change price')
                    count += 1
                    product.price = value[3]
                    check_prod = True
                    product.save()
            if not check_prod:
                count += 1
                create_category(value)
                print('Add prod')
        print('Finished successfull')




def create_category(myarr):
    check_cat = False
    category = Category.objects.all()

    for cat in category:
        if myarr[0] == cat.name and not check_cat:
            check_cat = True
            create_prod(myarr, cat)

    if not check_cat:
            check_cat = True
            create_cat(myarr)


def create_cat(myarr_cat):
    category = Category()
    category.name = myarr_cat[0]
    category.slug = myarr_cat[4]#Необходимо провверять slug на дубли
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