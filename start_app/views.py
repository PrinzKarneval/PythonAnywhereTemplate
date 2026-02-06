from django.views.generic import ListView

from .models import *


class CustomerListView(ListView):
    model = Customer