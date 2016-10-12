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
        file = open('newshop.txt', 'r')# открывает файл
        product = Product.objects.all()#получает объекты из модели
        for line in file:#пробегает по строкам из файла
            line.strip('\n')
            arr = line.split(';')#разделяет строку, испльзуя разделитель ;
            for p in product:# пробегает по массиву объектов, полученных из модели, для поиска совпадений объектов модели и выбранного наименования из файла.
                if int(arr[0]) == p.articul:  # сравнивает выбраное имя из файла и имя из массива модели.
                    check_goods = True  # если есть совпадение, переключаем, для перехода во внешний цикл, не заходя в следующее условие
            if not check_goods:
                create_category(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
            check_goods = False
            #print(arr[1])
        #file.close()
        self.stdout.write('Successfully')



def create_category(pr_artcl, pr_nm, category_name, pr_slg, ct_slg, pr_prc):
    category = Category.objects.all()
    for c in category:
        if c.name == category_name:
            create_prod(pr_artcl, pr_nm, c, pr_slg, pr_prc)
    my_category = Category()
    my_category.name = category_name
    my_category.slug = ct_slg
    my_category.save()
    create_prod(pr_artcl, pr_nm, my_category, pr_slg, pr_prc)


def create_prod(pr_articul, pr_name, pr_category, pr_slug, pr_price):
    print('prod')
    product = Product()
    product.articul = pr_articul
    product.name = pr_name
    product.category = pr_category
    product.slug = pr_slug
    product.price = float(pr_price)
    product.stock = 0
    product.available = True
    product.save()
    print('From create_prod')










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