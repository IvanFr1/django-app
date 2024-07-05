from typing import Any, Sequence
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from shopapp.models import Order, Product

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Create order with products')
        user = User.objects.get(username='admin')
        products: Sequence[Product] = Product.objects.defer("description", "price", "creted_at").all() # type: ignore
        products: Sequence[Product] = Product.objects.only("id", "name").all() # type: ignore
        order, created = Order.objects.get_or_create(
            delivery_address='ul Pupkina, d 8',
            promocode='SALE122352',
            user=user,
        )
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f'Created order {order}')