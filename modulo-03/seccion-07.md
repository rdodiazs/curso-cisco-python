# 7. Listas en aplicaciones avanzadas.

## 7.1 Listas en listas.

En Python es posible crear listas que poseen un nivel de complejidad mayor. En particular, establecer listas al interior de listas o, dicho de otro modo, listas con más de una dimensión. Estas corresponden a **arreglos** o *arrays*.

Un ejemplo de estructuras de datos como los arreglos, son las matrices. Desde su punto de vista más aplicado, corresponde a un arreglo con filas y columnas.

Existen tres maneras de llenar una lista. La primera es manual, pero es muy lenta. Otra opción es mediante algún bucle, como se observa en el siguiente ejemplo:

```python
lista_01 = []

for i in range(8):
    lista_01.append(i)

print(lista_01)
```

Al ejecutar el código de arriba, se obtiene lo siguiente:

```
[0, 1, 2, 3, 4, 5, 6, 7]
```

Una tercera manera, que es propia de Python (o más "pythonista"), para completar una lista con elementos es mediante la técnica de **comprensión de listas** (*list comprehension*). Consiste en lo siguiente:

```python
lista_01 = [i for i in range(8)]  # Técnica de comprensión de lista
print(lista_01)
```

Como se observa a continuación, se obtiene el mismo resultado:

```
[0, 1, 2, 3, 4, 5, 6, 7]
```

## 7.2 Arreglos bidimensionales.

Manejando cómo llenar una lista, sea mediante un bucle o a partir de la técnica de comprensión de lista, es posible crear arreglos (*arrays*) de mayor complejidad. En el siguiente código se construye una de **dos dimensiones**:

```python
lista_bidim = []

for i in range(8):
    filas = [i for i in range(8)]
    lista_bidim.append(filas)

print(lista_bidim)
```

Al ejecutar el código de arriba, se obtiene lo siguiente:

```
[[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]
```

Si ejecutamos el comando `print(len(lista_bidim))`, se apreciará que dicha lista consiste de 8 elementos que, en este caso, corresponden a 8 listas.

```
>>> print(len(lista_bidim))
8
```

Este proceso se puede hacer aún más corto aplicando solo el método de comprensión de lista, tal como se observa en el siguiente código:

```python
lista_bidim = [[i for i in range(8)] for j in range(8)]  # Comprensión de lista
print(lista_bidim)
```

Se obtiene el mismo resultado:

```
[[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]
```