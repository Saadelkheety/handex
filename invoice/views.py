from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from invoice.forms import CompanyForm, ClientForm, ProductForm, BalanceForm, InvoiceForm, InvoiceItemForm, InvoiceItemFormSet
from invoice.models import Company, Client, Product, Balance, Invoice, InvoiceItem

def index(request):
    return render(request, 'invoice/index.html')

# add or edit the company details
def company(request):
    context = {}
    if request.method == 'POST':
        try:
            company = Company.objects.all()[0]
            filled_form = CompanyForm(request.POST, instance=company)
            if filled_form.is_valid():
                print(company)
                filled_form.save()
        except Exception as e:
            filled_form = CompanyForm(request.POST)
            if filled_form.is_valid():
                filled_form.save()
        messages.success(request, 'Company details saved.')
        return render(request, 'invoice/index.html', context)
    else:
        try:
            company = Company.objects.all()[0]
            context["company"] = company
            form = CompanyForm(instance=company)
        except Exception as e:
            form = CompanyForm()
        context["form"] = form
        form = CompanyForm()
        return render(request, 'invoice/company_form.html', context)



# Client Crud

class ClientList(ListView):
    model = Client


class ClientCreate(CreateView):
    form_class = ClientForm
    template_name = "invoice/client_form.html"
    success_url = reverse_lazy('list_clients')
    def form_valid(self, form):
        context = {}
        messages.success(self.request, 'Client details saved.')
        return super().form_valid(form)


class ClientUpdate(UpdateView):
    form_class = ClientForm
    model = Client
    template_name = "invoice/client_form.html"
    success_url = reverse_lazy('list_clients')
    def form_valid(self, form):
        context = {}
        messages.success(self.request, 'Client details saved.')
        return super().form_valid(form)


class ClientDelete(DeleteView):
    success_url = reverse_lazy('list_clients')
    model = Client

    def get(self, *a, **kw):
        return self.delete(*a, **kw)


# Product Crud

class ProductList(ListView):
    model = Product


class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = "invoice/product_form.html"
    success_url = reverse_lazy('list_products')
    def form_valid(self, form):
        context = {}
        messages.success(self.request, 'Product details saved.')
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = "invoice/product_form.html"
    success_url = reverse_lazy('list_products')
    def form_valid(self, form):
        context = {}
        messages.success(self.request, 'Product details saved.')
        return super().form_valid(form)


class ProductDelete(DeleteView):
    success_url = reverse_lazy('list_products')
    model = Product

    def get(self, *a, **kw):
        return self.delete(*a, **kw)


# Balance Crud

class BalanceList(ListView):
    model = Balance


class BalanceCreate(CreateView):
    form_class = BalanceForm
    template_name = "invoice/balance_form.html"
    success_url = reverse_lazy('list_balance')
    def form_valid(self, form):
        context = {}
        messages.success(self.request, 'Balance details saved.')
        return super().form_valid(form)


class BalanceUpdate(UpdateView):
    form_class = BalanceForm
    model = Balance
    template_name = "invoice/balance_form.html"
    success_url = reverse_lazy('list_balance')
    def form_valid(self, form):
        context = {}
        messages.success(self.request, 'Balance details saved.')
        return super().form_valid(form)


class BalanceDelete(DeleteView):
    success_url = reverse_lazy('list_balance')
    model = Balance

    def get(self, *a, **kw):
        return self.delete(*a, **kw)


# invoice Crud
class InvoiceList(ListView):
    model = Invoice


class InvoiceCreate(CreateView):
    form_class = InvoiceForm
    model = Invoice
    template_name = "invoice/invoice_form.html"
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = InvoiceItemFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = InvoiceItemFormSet(self.request.POST)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))
