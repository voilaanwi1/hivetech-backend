from django.shortcuts import render
from rest_framework import generics

from apps.users.mixins import CustomLoginRequiredMixin
from .serializers import OrderItemListSerializer, OrderItemSerializer
from .models import OrderItem

# Create your views here.

from django.shortcuts import render
from rest_framework import generics

from apps.users.mixins import CustomLoginRequiredMixin
from .serializers import OrderItemListSerializer, OrderItemSerializer
from .models import OrderItem

class OrderList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = OrderItem.objects.order_by('-id').filter(user = request.login_user.id)
        return self.list(request, *args, **kwargs)

class OrderItemAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.login_user.id
        return super().create(request, *args, **kwargs)
