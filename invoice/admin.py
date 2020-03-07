from django.contrib import admin

from invoice.models import Company, Client

# Register your models here.
admin.site.register(Company)
admin.site.register(Client)
