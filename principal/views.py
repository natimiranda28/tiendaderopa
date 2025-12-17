from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Producto, Carrito

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"productos": productos})

@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    return render(request, "carrito.html", {
        "carrito_items": carrito_items,
        "total": total
    })
