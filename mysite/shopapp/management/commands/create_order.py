from typing import Any
from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Order

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Create order')
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address='ul Pupkina, d 8',
            promocode='SALE1223',
            user=user,
        )
        self.stdout.write(f'Created order {order}')