from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

class Workers(models.Model):
    name = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    worktitle = models.ForeignKey('WorkerJobTitle', related_name='workersjob', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return str(self.name)


class Change(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField(auto_now_add=True)
    orders = models.ManyToManyField('Order', related_name='rdrs')
    workers = models.ManyToManyField('Workers', related_name='workrws')

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return str(self.start)



class Product(models.Model):
    name = models.CharField(max_length=100, default='Безымянный')
    price = models.DecimalField(max_digits=100, decimal_places=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    chair = models.IntegerField(default=1)
    worker = models.ForeignKey('Workers', related_name='workr', on_delete=models.CASCADE)
    ordertime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=200, default='Занят')
    position = models.IntegerField(default=1)
    totalprice = models.DecimalField(max_digits=100, decimal_places=1)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.chair)

class WorkerJobTitle(models.Model):
    jobtitle = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return str(self.jobtitle)
