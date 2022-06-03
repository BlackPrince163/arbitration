from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="название")
    price = models.FloatField(verbose_name="цена")
    quantity = models.FloatField(verbose_name="количество")