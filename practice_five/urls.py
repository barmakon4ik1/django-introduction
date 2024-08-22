from django.urls import path, include
from practice_five.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'addresses', AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view(), name='products-list'),
    path('customers/', CustomerListCreateView.as_view(), name='customers-list'),
    path('orders/', OrderListCreateView.as_view(), name='orders-list'),
    path('order-items/', OrderItemsListCreateView.as_view(), name='order-items-list'),
    path('product-details/', ProductDetailListCreateView.as_view(), name='product-details-list'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyView.as_view(), name='products-retrieve-update-delete'),
    path('customers/<int:pk>', CustomerRetrieveUpdateDestroyView.as_view(), name='customers-retrieve-update-delete'),
    path('orders/<int:pk>', OrderRetrieveUpdateDestroyView.as_view(), name='orders-retrieve-update-delete'),
    path('order-items/<int:pk>', OrderItemsRetrieveUpdateDestroyView.as_view(),
         name='order-items-retrieve-update-delete'),
    path('product-details/<int:pk>', ProductDetailsRetrieveUpdateDestroyView.as_view(),
         name='product-details-retrieve-update-delete'),
]
