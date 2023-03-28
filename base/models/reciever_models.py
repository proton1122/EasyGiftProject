from django.db import models
import datetime
from django.contrib.auth import get_user_model
from base.models import Order


class Reciever(models.Model):
    Order = models.OneToOneField(Order, on_delete=models.CASCADE, blank=True, null=True)
    customer_name = models.CharField(default='', blank=True, max_length=50)
    customer_zipcode = models.CharField(default='', blank=True, max_length=8)
    customer_prefecture = models.CharField(default='', blank=True, max_length=50)
    customer_city = models.CharField(default='', blank=True, max_length=50)
    customer_address1 = models.CharField(default='', blank=True, max_length=50)
    customer_address2 = models.CharField(default='', blank=True, max_length=50)
    customer_tel = models.CharField(default='', blank=True, max_length=15)
    customer_mail = models.EmailField(default='', blank=True, max_length=70)