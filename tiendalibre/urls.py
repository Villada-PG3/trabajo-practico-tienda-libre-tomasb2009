from django.urls import path
from . import views

app_name = "tiendalibre"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalogo/", views.productos, name="catalogo"),
    path(
        "catalogo/<int:producto_id>/",
        views.detalle_producto,
        name="detalle_producto"
    ),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca-de-mi"),
]
