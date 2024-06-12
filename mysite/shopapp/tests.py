from string import ascii_letters
from random import choices
from django.test import TestCase
from django.urls import reverse
from shopapp.models import Order, Product
from shopapp.utils import add_two_numbers
from django.contrib.auth.models import User, Permission
from django.conf import settings

# Create your tests here.


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product_name = ''.join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

        self.user = User.objects.create_user(username='testuser', password='qwerty')

        permission = Permission.objects.get(codename='add_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='qwerty')
    
    def test_product_create_view(self):
        response = self.client.post(
           reverse('shopapp:product_create'),
           {
                "name": self.product_name,
                "price": '123.45',
                "description": 'A good table',
                "discount": '10',

           }
        )
        self.assertRedirects(response, reverse('shopapp:products_list'))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name='Best Product')

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    def test_product_detail_view(self):
        response = self.client.get(
            reverse('shopapp:product_details', kwargs={'pk': self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_and_check_content(self):
        response = self.client.get(
            reverse('shopapp:product_details', kwargs={'pk': self.product.pk})
        )
        self.assertContains(response, self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        'users-fixture.json',
        'groups-fixture.json',
        'products-fixture.json',
    ]

    def test_products(self):
        response = self.client.get(reverse('shopapp:products_list'))
        
        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context['products']),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, 'shopapp/products-list.html')


class OrdersListViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='bob_test', password='qwerty')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertContains(response, 'Orders')

    def test_orders_view_not_authentificated(self):
        self.client.logout()
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url) # type: ignore


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'users-fixture.json',
        'groups-fixture.json',
        'products-fixture.json',
    ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse('shopapp:products-export'),
        )

        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by('pk').all()

        expected_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': str(product.price),
                'archived': product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data['products'],
            expected_data
        )


class OrderDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='user_test', password='qwerty')
        permission = Permission.objects.get(codename='view_order')
        cls.user.user_permissions.add(permission)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.login(username='user_test', password='qwerty')
        self.order = Order.objects.create(
            delivery_address = '458 Test st',
            promocode = 'TESTPROMO',
            user = self.user,
        )

    def tearDown(self):
        self.order.delete()


    def test_order_details(self):
        response = self.client.get(reverse('shopapp:order_details', args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.delivery_address) # type: ignore
        self.assertContains(response, self.order.promocode)
        self.assertEqual(response.context['object'].pk, self.order.pk)


class OrdersExportTestCase(TestCase):

    fixtures = [
        'users-fixture.json',
        'products-fixture.json',
        'order-fixture.json',
        'groups-fixture.json',
    ]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='user1_test', password='qwerty')
        cls.user.is_staff = True
        cls.user.save()
    
    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cls.user.delete()

    def setUp(self) -> None:
        super().setUp()
        self.client.force_login(self.user)

    def test_orders_list(self):
        response = self.client.get(
            reverse(
                'shopapp:orders-export',
                )
        )

        self.assertEqual(response.status_code, 200)

        orders = Order.objects.order_by('pk').all()

        expected_data = [
            {
                'pk': order.pk,
                'delivery_address': order.delivery_address,
                'promocode': order.promocode,
                'user': order.user.pk,
                'products': [product.pk for product in order.products.all()],
            }
            for order in orders
        ]

        orders_data = response.json()

        self.assertEqual(
            orders_data['orders'],
            expected_data
        )
