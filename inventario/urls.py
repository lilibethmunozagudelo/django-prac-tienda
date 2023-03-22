from django.urls import path
from inventario.views import *
urlpatterns=[path("inventario/",inventario, name="inventario")]