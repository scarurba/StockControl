from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm

@login_required 
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compra/listar_productos.html', {'productos': productos})

@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()  
    return render(request, 'compra/listar_proveedores.html', {'proveedores': proveedores})

@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'compra/proveedor_form.html', {'form': form})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra:listar_productos')
    else:
        form = ProductoForm()
        proveedores = Proveedor.objects.all()
    return render(request, 'compra/producto_form.html', {'form': form, 'proveedores': proveedores})


