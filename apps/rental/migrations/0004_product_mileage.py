# Generated by Django 4.0.5 on 2022-06-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mileage',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
