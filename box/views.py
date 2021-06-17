from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import permissions
from rest_framework.mixins import  CreateModelMixin
from .models import *
from .serializers import *

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderCreateSet(CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     author = get_object_or_404(CoffeePoint, id=self.request.data.get('author_id'))
    #     return serializer.save(author=author)


class CoffeePointSet(ReadOnlyModelViewSet):
    queryset = CoffeePoint.objects.prefetch_related('coffee').all()
    serializer_class = CoffeePointSerializer