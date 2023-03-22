from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('carrito_compras', include('carrito_compras.urls')),
    path('admin/', admin.site.urls),
]
