from django.db import models
from django.contrib.auth.decorators import login_required
""" from .models import Carrito """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Producto



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.nombre
"""Aca hice eliminar carrito"""
@login_required
def eliminar_del_carrito(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Carrito, id=item_id, usuario=request.user)
        item.delete()
    return redirect('ver_carrito')

""" Aca voy a crear para guardar una orden:  """

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"

class ItemOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"