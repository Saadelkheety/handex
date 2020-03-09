from django.contrib import admin

from invoice.models import Company, Client, Product, Balance,Invoice, InvoiceItem


class InvoiceItemInline(admin.TabularInline):
      model = InvoiceItem
      extra = 1


class InvoiceAdmin(admin.ModelAdmin):
      inlines = [InvoiceItemInline]


# Register your models here.
admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Balance)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem)
