from typing import Any
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from shopapp.models import Product

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Start demo select fields')

        users_info = User.objects.values_list("username", flat=True)
        print(list(users_info))
        for user_info in users_info:
            print(user_info)

        product_values = Product.objects.values("pk", "name")
        for p_values in product_values:
            print(p_values)

        self.stdout.write('Done')
