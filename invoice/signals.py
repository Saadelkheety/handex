from django.db.models.signals import post_save
from django.dispatch import receiver
from invoice.models import Payment, Invoice


@receiver(post_save, sender=Payment)
def payment_added(sender, instance, **kwargs):
    invoice = instance.invoice
    amountpaid = invoice.amountPaid()
    amountdue = invoice.amountDue()
    if amountpaid >= amountdue:
        invoice.paid = True
