# Generated by Django 4.0.5 on 2022-06-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_product_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mileage',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
