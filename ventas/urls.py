from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ventas', include('ventas.urls')),
    path('admin/', admin.site.urls),
]
