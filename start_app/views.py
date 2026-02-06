from django.views.generic import ListView

from .models import *


class CustomerList(ListView):
    model = Customer