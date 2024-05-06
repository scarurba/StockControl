from django.urls import path
from django.views.generic import TemplateView

from .views import listar_productos, listar_proveedores, crear_producto, crear_proveedor

app_name = 'compra'

urlpatterns = [
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('listar_proveedores/', listar_proveedores, name='listar_proveedores'),
    path('producto_form/', crear_producto, name='producto_form'),
    path('proveedor_form/', crear_proveedor, name='proveedor_form'),
    path('', TemplateView.as_view(template_name='base/index.html'), name='index'),
]