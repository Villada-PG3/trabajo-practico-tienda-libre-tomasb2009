# Consultas ORM - Django Shell

## 1. Obtener todos los productos

```
Producto.objects.all()
```

Obtiene todos los productos registrados en la base de datos.

---

## 2. Productos con precio mayor a 1000

```
Producto.objects.filter(precio__gt=1000)
```

Utiliza el lookup `__gt` para buscar productos cuyo precio sea mayor a 1000.

---

## 3. Productos con precio menor a 5000

```
Producto.objects.filter(precio__lt=5000)
```

Utiliza el lookup `__lt` para buscar productos cuyo precio sea menor a 5000.

---

## 4. Productos cuyo nombre contiene "iphone"

```
Producto.objects.filter(nombre__icontains="iphone")
```

Utiliza `__icontains` para buscar productos cuyo nombre contenga "iphone", sin distinguir entre mayúsculas y minúsculas.

---

## 5. Excluir productos sin stock

```
Producto.objects.exclude(stock=0)
```

Devuelve todos los productos excepto aquellos que tienen stock igual a 0.

---

## 6. Ordenar productos por precio

```
Producto.objects.order_by("precio")
```

Ordena los productos por precio de menor a mayor.

Para ordenar de mayor a menor:

```
Producto.objects.order_by("-precio")
```

---

## 7. Buscar productos de determinadas marcas

```
Producto.objects.filter(marca__in=["Samsung", "Apple", "Xiaomi"])
```

Utiliza `__in` para buscar productos cuya marca coincida con alguno de los valores indicados.

---

## 8. Acceder a la categoría desde un producto

```
producto = Producto.objects.first()
producto.categoria
```

Permite acceder a la categoría relacionada con un producto.

También se puede obtener el nombre de la categoría:

```
producto.categoria.nombre
```

---

## 9. Acceder a los productos desde una categoría

```
categoria = Categoria.objects.first()
categoria.productos.all()
```

Gracias a `related_name="productos"`, se pueden obtener todos los productos pertenecientes a una categoría.

---

## 10. Buscar un producto utilizando get()

```
producto = Producto.objects.get(id=1)
```

`get()` devuelve directamente un único objeto. Si no existe ningún objeto con ese ID, produce una excepción `DoesNotExist`. Si encuentra más de uno, produce `MultipleObjectsReturned`.

A diferencia de `get()`, `filter()` devuelve un QuerySet.
