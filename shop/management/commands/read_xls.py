from django.core.management import BaseCommand
from shop.models import Product, Category
import xlrd, xlwt


class Command(BaseCommand):
    help = 'read xls file'

    def handle(self, *args, **options):

        # открываем файл
        rb = xlrd.open_workbook('test.xls', formatting_info=True)

        # выбираем активный лист
        sheet = rb.sheet_by_index(0)
        vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
        for i in vals:
            print(i)