# Generated by Django 4.1.7 on 2023-03-26 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_rename_sales_sale_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]