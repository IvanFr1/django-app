from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
                    ShopIndexView, 
                    GroupListView, 
                    ProductDetailsView,
                    ProductsListView,
                    OrdersListView,
                    OrderDetailView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,
                    OrderCreateView,
                    OrderUpdateView,
                    OrderDeleteView,
                    ProductsDataExportView,
                    OrdersDataExportView,
                    ProductViewSet,
                    OrderViewSet,
                    LatestPrductsFeed,
)



app_name = 'shopapp'

routers = DefaultRouter()
routers.register('products', ProductViewSet)
routers.register('orders', OrderViewSet)

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('api/', include(routers.urls)),
    path('groups/', GroupListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/export', ProductsDataExportView.as_view(), name='products-export'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/archived/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_details'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/export/', OrdersDataExportView.as_view(), name='orders-export'),
    path('products/<int:pk>/confirm-delete/', OrderDeleteView.as_view(), name='order_delete'),
    path("products/latest/feed/", LatestPrductsFeed(), name='products-feed'),
]
