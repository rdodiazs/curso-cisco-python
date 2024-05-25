# 6. Operaciones en listas.

## 6.2. Cortes (*slices*) poderosos.


Al trabajar con listas, se debe tener en cuenta que cuando es asignada a una variable, lo que **se almacena en la RAM es su nombre, pero no su contenido**. Veamos el siguiente ejemplo:

```
>>> lista_01 = [1]
>>> lista_02 = lista_01
>>> lista_01[0] = [2]
>>> print(lista_02)
[2]
```

Como se observa en el ejemplo de arriba, aunque asignamos la variable `lista_01` a `lista_02` antes de modificar a la primera, luego de cambiar el valor de `lista_01`, de igual modo `lista_02 = [2]`. El motivo es lo que se señaló al inicio de esta sección: En `lista_02 = lista_01`, lo que se almacenó en la memoria fue el nombre `lista_02`, pero no se trasladó el valor de `lista_01` a dicha ubicación.

Para evitar el problema visto en el anterior ejemplo, es recomendado usar el **método de corte** o ***slice*** para almacenar uno o todos los elementos de una lista en otra variable, sin que esta nueva variable cambie al modificar a la original. En Python, se hace de la siguiente manera:

```
>>> lista_01 = [1]
>>> lista_02 = lista_01[:]
>>> lista_01[0] = 2
>>> print(lista_02)
[1]
```

La sintáxis del slice de una lista es la siguiente:

```python
lista_01[inicio:fin]
```

donde `inicio:fin` corresponde a los índices de la lista que queremos "cortar", que van **desde `inicio` hasta el anterior a `fin`**. Si no se indican dichos valores, se hará slice desde el primer elemento hasta el último.

También es posible usar **indices negativos** en la técnica del slice. Al utilizarlo, se indica qué **elementos se quieren excluir** de ser "cortados". Por ejemplo,

```
>>> lista_01 = [1, 2, 5, 3, 4]
>>> print(lista_01[0:-1])
[1, 2, 5, 3]
```

En este caso, el índice `-1` corresponde a la ubicación del último elemento de una lista, de izquierda a derecha. Al usarlo en un slice, se está indicando que no se quiere añadirlo en el "corte".

La técnica del slice también se puede utilizar **en conjunto con la palabra clave `del`**. Principalmente, **para eliminar un rango de elementos** de una lista.

```
>>> lista_01 = [10, 8, 6, 4, 2]
>>> del lista_01[1:3]
>>> print(lista_01)
[10, 4, 2]
```


## 6.4 Los operadores `in` y `not in`.

A partir de los operadores `in` y `not in`, es posible saber si existe o no un elemento en una lista. Esto implica que, como resultado, entregan un valor booleano.

```
>>> mi_lista = [2, 5, 6, 1, 3]
>>> print(8 in mi_lista)
False
>>> print(8 not in mi_lista)
True
>>> print(2 in mi_lista)
True
```

