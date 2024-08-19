from django.urls import path
from practice_five.views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
]