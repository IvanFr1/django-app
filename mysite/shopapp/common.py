from .models import Product
from .models import Order
from django.contrib.auth.models import User


from csv import DictReader
from io import TextIOWrapper


def save_csv_products(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    products = [
            Product(**row)
            for row in reader
        ]
    Product.objects.bulk_create(products)
    return products

def save_csv_orders(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)

    orders = []

    for row in reader:

        user = User.objects.get(pk=int(row['user']))
        order = Order(
            delivery_address=row['delivery_address'],
            promocode=row['promocode'],
            user=user
        )
        order.save()

        product_ids = row['products'].split(',')
        products = Product.objects.filter(id__in=product_ids)
        order.products.set(products)

        orders.append(order)


    return orders