
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from .models import Producto


class HomeView(TemplateView):
    template_name = "tiendalibre/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo"] = "Productos destacados"
        context["usuario_logueado"] = False
        context["productos_destacados"] = Producto.objects.order_by(
            "-fecha_creacion"
        )[:3]

        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "tiendalibre/catalogo.html"
    context_object_name = "productos"
    ordering = ["-fecha_creacion"]


def acerca_de_mi(request):
    from django.shortcuts import render
    return render(request, "tiendalibre/acerca-de-mi.html")


def detalle_producto(request, producto_id):
    from django.shortcuts import render

    producto = get_object_or_404(Producto, id=producto_id)

    contexto = {
        "producto": producto
    }

    return render(request, "tiendalibre/detalle_producto.html", contexto)
