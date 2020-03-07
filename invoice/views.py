from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from invoice.forms import CompanyForm, ClientForm, ProductForm
from invoice.models import Company, Client, Product

def index(request):
    return render(request, 'invoice/index.html')

# add or edit the company details
def company(request):
    context = {}
    if request.method == 'POST':
        filled_form = CompanyForm(request.POST)
        if filled_form.is_valid():
            created_company = filled_form.save()
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
