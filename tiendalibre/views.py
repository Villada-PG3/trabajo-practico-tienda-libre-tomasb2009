""" from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProductosTemplateView(TemplateView):
    template_name = "productos.html" """

from datetime import date

from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto


def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "tiendalibre/productos.html", contexto)


def home(request):
    productos_destacados = [
        {
            'nombre': 'notebook lenovo ideapad',
            'precio': 450000,
            'stock': 8,
            'descripcion': 'Notebook liviana ideal para uso diario, con buena batería y pantalla Full HD de 15 pulgadas.',
            'fecha_ingreso': date(2026, 7, 20),
        },
        {
            'nombre': 'mouse inalámbrico logitech',
            'precio': 12500,
            'stock': 0,
            'descripcion': 'Mouse ergonómico con conexión Bluetooth y USB, batería de larga duración.',
            'fecha_ingreso': date(2026, 6, 15),
        },
        {
            'nombre': 'teclado mecánico redragon',
            'precio': 38000,
            'stock': 3,
            'descripcion': 'Teclado mecánico retroiluminado RGB con switches azules.',
            'fecha_ingreso': date(2026, 8, 1),
        },
        {
            'nombre': 'monitor samsung 24 pulgadas',
            'precio': 210000,
            'stock': 12,
            'descripcion': 'Monitor Full HD con panel IPS, ideal para trabajo y diseño.',
            'fecha_ingreso': date(2026, 5, 10),
        },
        {
            'nombre': 'auriculares bluetooth sony',
            'precio': 95000,
            'stock': 20,
            'descripcion': 'Auriculares con cancelación de ruido activa y hasta 30 horas de batería.',
            'fecha_ingreso': date(2026, 8, 25),
        },
        {
            'nombre': 'silla gamer secretlab',
            'precio': None,
            'stock': 5,
            'descripcion': 'Silla ergonómica reclinable, próximamente disponible con nuevo precio de lanzamiento.',
            'fecha_ingreso': date(2026, 8, 28),
        },
    ]

    context = {
        'titulo': 'Productos destacados',
        'usuario_logueado': False,
        'productos_destacados': productos_destacados,
    }
    return render(request, "tiendalibre/home.html", context)


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca-de-mi.html")
