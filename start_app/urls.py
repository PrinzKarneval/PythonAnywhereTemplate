from django.urls import path

urlpatterns = [
    path('', CustomerList.as_view(), name='customer_list'),
]
