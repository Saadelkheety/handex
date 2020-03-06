from django.db import models


# Company : Name + Adress + Tel + VAT
class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField(blank=True)
    tel = models.CharField(max_length=32)
    vat = models.CharField(max_length=256)


# Client : code + name + adress + initial balance
class Client(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64)
    address = models.TextField(blank=True)


# Client Balance : Client Name + Total Sales + Total Payments + Balance (initial balance+Sales-Payments)
class Balance(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    sales = models.FloatField()
    payments = models.FloatField()
    balance = models.FloatField()


# Product : code + product name + price
class Product(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    price = models.FloatField()


 # invoice : invoice number +date + client name + client adress + product
 # + price + total + total invoice + VAT + Total VAT (total invoice * VAT)
 # + general Total invoice (Total invoice + Total VAT)
class Invoice(models.Model):
    number = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    total = models.FloatField()


class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateField(auto_now=True)


 # payment : date + client name + invoice + amount paid + amount due
class Payment(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    amountDue = models.FloatField()
    amountPaid = models.FloatField()
    date = models.DateField(auto_now_add=True)
