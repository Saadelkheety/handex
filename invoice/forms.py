from django.forms import ModelForm, inlineformset_factory
from invoice.models import Company, Client, Product, Balance, Invoice, InvoiceItem, Payment

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
        exclude = ('paid',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'rows': '3'})
        try:
            vat = Company.objects.all()[0].vat
        except Exception as e:
            pass
        self.fields['vat'].widget.attrs.update({'value':vat})


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['invoice'].queryset = Invoice.objects.filter(paid=False)


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = "__all__"


InvoiceItemFormSet = inlineformset_factory(Invoice,
    InvoiceItem,
    form=InvoiceItemForm,
    extra=3,
    can_delete=False)
