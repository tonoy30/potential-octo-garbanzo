# Generated by Django 4.0.5 on 2022-06-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_product_rent_expire_at_product_rented_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rent_expire_at',
            new_name='returned_at',
        ),
    ]
