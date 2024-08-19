from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from practice_five.models import Product
from practice_five.serializers import ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 2


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
