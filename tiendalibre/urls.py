from django.urls import path
from tiendalibre.views import HomeView, CatalogoView, acerca_de_mi, detalle_producto

app_name = "tiendalibre"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("catalogo/", CatalogoView.as_view(), name="catalogo"),
    path("acerca-de-mi/", acerca_de_mi, name="acerca-de-mi"),
    path("producto/<int:producto_id>/", detalle_producto, name="detalle_producto"),
]