from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomerList.as_view(), name='customer_list'),
]
