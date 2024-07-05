from typing import Any
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Count, Sum
from shopapp.models import Product, Order

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Start demo aggregate')

        # result = Product.objects.filter(
        #     name__contains="Smartphone"
        # ).aggregate(
        #     Avg("price"),
        #     Max("price"),
        #     min_price=Min("price"),
        #     count=Count("id"),
        # )
        # print(result)
        orders = Order.objects.annotate(
            total=Sum("products__price", default=0),
            products_count=Count("products"),
        )
        for order in orders:
            print(
                f"Order #{order.id}" # type: ignore
                f"with {order.products_count}" # type: ignore
                f"products worth {order.total}" # type: ignore
            )
        self.stdout.write('Done')