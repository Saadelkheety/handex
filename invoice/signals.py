from django.db.models.signals import post_save
from django.dispatch import receiver
from invoice.models import Payment, Invoice, Balance, Client


@receiver(post_save, sender=Payment)
def payment_added(sender, instance, **kwargs):
    invoice = instance.invoice
    amountpaid = invoice.amountPaid()
    amountdue = invoice.amountDue()
    totaldue = (invoice.vat/100)*amountdue+amountdue
    if amountpaid >= totaldue:
        invoice.paid = True


@receiver(post_save, sender=Client)
def add_balance(sender, instance, **kwargs):
    balance = Balance(client=instance)
    try:
        balance.save()
    except Exception as e:
        pass
