# 4. Listas.

## 4.1 ¿Qué son las listas?

En ocasiones, en vez de asignar muchas variables a distintos valores es preferible hacer lo mismo, pero en solo una variable. Es decir, definir una variable como un conjunto de valores. En Python, aquello es posible mediante una estructura de datos conocida como **lista**.

A continuación vemos una lista con valores de distinto tipo asignada a una variable llamada `lista_01`.

```python
lista_01 = [1, "a", 2]
```

A cada elemento de una lista se le asigna un **índice** según su posición en ella, el cual comienza desde el `0`. Por lo tanto, se dice que una lista es de tipo "**índice cero**" (en inglés se dice que es *zero-index*).


## 4.3 Accediendo y modificando los elementos de una lista.

Es posible acceder individualmente a los elementos de una lista escribiendo su índice adentro de paréntesis "`[ ]`". Por ejemplo, si queremos obtener el primer elemento de `lista_01 = [1, "a", 2]`, lo hacemos como:

```
>>> lista_01 = [1, "a", 2]
>>> print(lista_01[0])
1
```

Mediante la función `len()`, se puede conocer la cantidad de elementos (o longitud) de una lista:

```
>>> lista_01 = [1, "a", 2]
>>> print(len(lista_01))
3
```

Las listas son **modificables**. Por ejemplo, es posible cambiar el valor de un elemento indicando su índice, como lo vemos a continuación.

```
>>> lista_01 = [1, "a", 2]
>>> print(lista_01[2])
2
>>> lista_01[2] = 10
>>> print(lista_01[2])
10
```

También, mediante la palabra clave **`del`** es posible **eliminar** un elemento de una lista. Por ejemplo, a continuación quitamos el segundo elemento de la lista `lista_01`.

```
>>> lista_01 = [1, "a", 2]
>>> del lista[1]
>>> print(lista_01)
[1, 2]
>>> print(len(lista_01))
2
```


## 4.8 Métodos para añadir elementos a una lista: `append()` e `insert()`.

Para agregar elementos a una lista, podemos usar dos métodos: `append()` y `insert()`. A continuación se ilustran sus sintáxis, donde `lista_01` es una lista cualquiera.

```
lista_01.append(valor)

lista_01.insert(valor, posicion)
```

Como se observa, el método `insert()` es similar a `append()`, pero más preciso porque uno puede indicar dónde agregar el elemento en una lista. En cambio, `append()` la añade automáticamente después de su **último elemento**.


