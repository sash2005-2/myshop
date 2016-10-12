# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('quantity',), 'verbose_name': 'количество', 'verbose_name_plural': 'количество'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]
