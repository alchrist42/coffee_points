from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import permissions
from rest_framework.mixins import  CreateModelMixin
from .models import *
from .serializers import *


class OrderCreateSet(CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CoffeePointSet(ReadOnlyModelViewSet):
    queryset = CoffeePoint.objects.prefetch_related('coffee').all()
    serializer_class = CoffeePointSerializer