from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import PositiveIntegerField
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.fields.related import ForeignKey


class CoffeeType(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class CoffeePoint(models.Model):
    title = models.CharField(max_length=64)
    place = models.CharField(max_length=256, blank=True)
    coffee = models.ManyToManyField(CoffeeType, related_name='points', blank=True)

    def __str__(self):
        return f'{self.title} ({self.place})'


class Order(models.Model):
    VOLUME_CHOICES = (
        (0.2, 'small'),
        (0.3, 'medium'),
        (0.5, 'large')
    )
    coffee = ForeignKey(CoffeeType, on_delete=CASCADE, related_name='orders')
    point = ForeignKey(CoffeePoint, on_delete=CASCADE, related_name='orders')
    # customer = ForeignKey(User)
    customer = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    volume = models.FloatField(choices=VOLUME_CHOICES, default=0.2)

    class Meta:
        ordering = ('done', '-created',)

    def __str__(self):
        return f'({self.created.strftime("%H:%M:%S %d %b")})\t{self.customer.title()}: {self.volume} {self.coffee}. {self.done}.' 