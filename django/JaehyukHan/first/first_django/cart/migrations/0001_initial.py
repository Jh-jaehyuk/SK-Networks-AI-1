# Generated by Django 5.0.6 on 2024-06-20 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
        ("product", "0002_product_productimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("cartId", models.AutoField(primary_key=True, serialize=False)),
                ("createdDate", models.DateTimeField(auto_now_add=True)),
                ("updatedDate", models.DateTimeField(auto_now=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carts",
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "cart",
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                ("cartItemId", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="cart.cart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={
                "db_table": "cart_item",
            },
        ),
    ]
