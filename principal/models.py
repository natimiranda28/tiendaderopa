from django.db import models
from django.contrib.auth.decorators import login_required
from .models import Carrito
from django.shortcuts import render, redirect, get_object_or_404



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.nombre

@login_required
def eliminar_del_carrito(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Carrito, id=item_id, usuario=request.user)
        item.delete()
    return redirect('ver_carrito')

