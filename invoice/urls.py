from django.urls import path

from invoice import views

urlpatterns = [
    path("", views.index, name="index"),
    path("company/", views.company, name="company"),
    path("clients/", views.ClientList.as_view(), name="list_clients"),
    path("create_client/", views.ClientCreate.as_view(), name="create_client"),
    path("update_client/<int:pk>/", views.ClientUpdate.as_view(), name="update_client"),
    path("delete_client/<int:pk>/", views.ClientDelete.as_view(), name="delete_client"),
    path("products/", views.ProductList.as_view(), name="list_products"),
    path("create_product/", views.ProductCreate.as_view(), name="create_product"),
    path("update_product/<int:pk>/", views.ProductUpdate.as_view(), name="update_product"),
    path("delete_product/<int:pk>/", views.ProductDelete.as_view(), name="delete_product"),
]
