from django.forms import ModelForm, inlineformset_factory
from invoice.models import Company, Client, Product, Balance, Invoice, InvoiceItem

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        labels = {
            "name": "Company name",
            "address": "Company Address",
            "tel": "Company telephone number",
            "vat": "Company Vat"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'rows': '3'})


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        labels = {
            "initialBalance": "Initial Balance"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'rows': '3'})


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class BalanceForm(ModelForm):
    class Meta:
        model = Balance
        fields = "__all__"


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = "__all__"


InvoiceItemFormSet = inlineformset_factory(Invoice,
    InvoiceItem,
    form=InvoiceItemForm,
    extra=3,
    can_delete=False)
