from timeit import default_timer
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse # type: ignore
from django.contrib.auth.models import Group
from .models import Product, Order, ProductImage
from .forms import  GroupForm, ProductForm, OrderForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            'time_running': default_timer(),
            'products': products,
            'items': 1,
        }
        return render(request, 'shopapp/shop-index.html', context=context)

class GroupListView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)
    
    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class ProductDetailsView(DetailView):
    template_name = 'shopapp/products-details.html'
    # model = Product
    queryset = Product.objects.prefetch_related('images')
    context_object_name = 'product'
    

class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = 'products'
    queryset = Product.objects.filter(archived=False)
    

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
 
    model = Product
    fields = 'name', 'price', 'description', 'discount', 'preview'
    success_url = reverse_lazy('shopapp:products_list')

    def test_func(self):
        return self.request.user.has_perm('shopapp.add_product') # type: ignore
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    # fields = 'name', 'price', 'description', 'discount', 'preview'
    template_name_suffix = '_update_form'
    form_class = ProductForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if not (user.is_superuser or (user.has_perm('change_product') or user == obj.created_by)): # type: ignore
            raise PermissionDenied('You don`t have permission to change this product')
        return obj

    def get_success_url(self):
        return reverse(
            'shopapp:product_details',
            kwargs={'pk': self.object.pk}, # type: ignore
        )
        
    def form_valid(self, form: ProductForm) -> HttpResponse:
        response = super().form_valid(form)
        
        for image in self.request.FILES.getlist('images'):

            ProductImage.objects.create(
                product=self.object, # type: ignore
                image=image,
            )
    
        return response


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True # type: ignore
        self.object.save() # type: ignore
        return HttpResponseRedirect(success_url)
    

class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related('products')
    )

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['shopapp.view_order']
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related('products')
    )


class OrderCreateView(CreateView):
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    success_url = reverse_lazy('shopapp:orders_list')


class OrderUpdateView(UpdateView):
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:order_details',
            kwargs={'pk': self.object.pk}, # type: ignore
        )
    

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('shopapp:orders_list')


class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by('pk').all()
        products_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': product.price,
                'archived': product.archived,
            }
            for product in products
        ]
        return JsonResponse({'products': products_data})
    

class OrdersDataExportView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff # type: ignore

    def get(self, request: HttpRequest) -> JsonResponse:

        orders = Order.objects.order_by('pk').all()

        orders_data = [
            {
                'pk': order.pk,
                'delivery_address': order.delivery_address,
                'promocode': order.promocode,
                'user': order.user.pk,
                'products': [product.pk for product in order.products.all()],
            }
            for order in orders
        ]

        return JsonResponse({'orders': orders_data})