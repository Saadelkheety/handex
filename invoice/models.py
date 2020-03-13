from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Company : Name + Adress + Tel + VAT


class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField(blank=True)
    tel = models.CharField(max_length=32)
    vat = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)],)

    def __str__(self):
        return f"{self.name} company"

# Client : code + name + adress + initial balance


class Client(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64, unique=True)
    address = models.TextField()
    initialBalance = models.FloatField()

    def __str__(self):
        return f"{self.name}"


# Client Balance : Client Name + Total Sales + Total Payments + Balance (initial balance+Sales-Payments)
class Balance(models.Model):
    client = models.OneToOneField('Client', on_delete=models.CASCADE)
    # balance = models.FloatField()

    def sales(self):
        invoices = self.client.invoice_set.all()
        sales_amount = 0.0
        for invoice in invoices:
            sales_amount += invoice.amountDue()
        return sales_amount

    def payments(self):
        invoices = self.client.invoice_set.all()
        payments_amount = 0.0
        for invoice in invoices:
            payments_amount += invoice.amountPaid()
        return payments_amount

    def __str__(self):
        return f"{self.client.name} balance"


# Product : code + product name + price
class Product(models.Model):
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.price}$)"

 # invoice : invoice number +date + client name + client adress + product
 # + price + total + total invoice + VAT + Total VAT (total invoice * VAT)
 # + general Total invoice (Total invoice + Total VAT)


class Invoice(models.Model):
    date = models.DateField(default=timezone.now)
    number = models.CharField(max_length=64, unique=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    vat = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)],)

    def amountDue(self):
        items = self.invoiceitem_set.all()
        amount_due = 0.0
        for item in items:
            amount_due += (item.price * item.quantity)
        return amount_due

    def amountPaid(self):
        payments = self.payment_set.all()
        amount_paid = 0.0
        for payment in payments:
            amount_paid += payment.amountPaid
        return amount_paid


    def __str__(self):
        return f"invoice number: {self.number} of client {self.client}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.product} for {self.invoice}"
 # payment : date + client name + invoice + amount paid + amount due


class Payment(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    amountPaid = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"payment of {self.invoice}"
