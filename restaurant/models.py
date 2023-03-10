from django.utils import timezone
from django.db import models

from datetime import time


RESERVATION_SLOT = [
    (14, '14:00:00'),
    (15, '15:00:00'),
    (16, '16:00:00'),
    (17, '17:00:00'),
    (18, '18:00:00'),
    (19, '19:00:00'),
    (20, '20:00:00'),
    (21, '21:00:00'),
    (22, '22:00:00'),
]


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(choices=RESERVATION_SLOT, default=22)

    class Meta:
        unique_together = ['reservation_date', 'reservation_slot']

    def __str__(self):
        return self.first_name


class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return self.name