from django.contrib import admin

# Register your models here.
from compra.models import Proveedor, Producto

admin.site.register(Proveedor),
admin.site.register(Producto),
