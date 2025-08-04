from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantity in stock')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    surname = models.CharField('Surname', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return self.name

