# 6. Tuplas y Diccionarios.

## 6.1 Tipos de secuencias y mutabilidad.

En el módulo 3 ([sección 04](../modulo-03/seccion-04.md)) estudiamos a una estructura de datos conocida como **lista**, que puede ser entendida como aquella que permite almacenar varios datos. En el lenguaje Python existen más de ellas y son agrupadas bajo el concepto de **secuencias**.

Las **secuencias** son tipos de datos que **permiten almacenar más de un valor o menos de uno** (es posible tener conjuntos vacíos) y estos elementos pueden ser **leídos secuencialmente uno por uno**.

Una herramienta que es muy útil para leer los elementos de una secuencia, es el búcle `for`. Por ejemplo, si se ejecuta el siguiente código:

```python
colores = ["rojo", "azul", "verde", "negro"]

for color in colores:
    print(color)

```

Se obtiene:

```
rojo
azul
verde
negro
```

Un concepto que se vincula a las secuencias (pero no es exclusivo a ellas) es el de **mutabilidad**. Es una propiedad de algunos tipos de datos cuando pueden ser **modificados durante el proceso de ejecución de un programa**. En los casos donde aquello no es posible, se dice que el tipo de dato es **inmutable**.

Cuando se modifica un dato mutable, en Python dicho proceso recibe el nombre de **operación *in-situ***.


## 6.2 Tuplas.

Un segundo tipo de secuencia que existe en Python (además de las listas) son las **tuplas**.

Una tupla es definida mediante **paréntesis redondos**. Es decir, a partir de "`( )`". A continuación vemos una:

```python
tupla_01 = ("a", 2, True)
```

Las tuplas también pueden ser definidas sin los paréntesis, pero sus elementos **deben ser separados con comas**.

```
>>> tupla_01 = "a", 2, True
>>> print(tupla_01)
('a', 2, True)
```

Además del tipo de paréntesis que se utilizan para ser definidas, las **tuplas** también **se diferencian de las listas** en que las primeras **son inmutables**. Esto significa que, por ejemplo, no es posible utilizar en ellas los métodos `.append()` o `.insert()`.

```
>>> tupla_01 = ("a", 2, True)
>>> tupla_01.append("c")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
```

Sin embargo, hay funciones y operadores usados en las listas que también se pueden aplicar a las tuplas. A continuación se enlistan algunas de ellas:

- Es posible usar la función `len()` para contar los elementos de una tupla.
- El operador `+` puede ser usado para unir dos tuplas (también es posible con las listas).
- Al usar el operador `*` entre un valor entero (`int`) y una tupla (o una lista), sus elementos se repiten en el mismo orden la cantidad de veces de dicho `int`.
- Se pueden usar las palabras claves `in` y `not in` para evaluar si un elemento existe o no en una tupla.


## 6.3 Diccionarios.

Una estructura de datos que no es una secuencia, pero que aún así permite almacenar varios valores en ella, es el **diccionario**.

Los diccionarios en Python son una estructura de datos que siguen el formato **clave-valor** (*key-value*) y se definen mediante los caracteres "`{ }`". En el siguiente código se muestra un ejemplo:

```python
verduleria = {
    "Fruta": "Manzana",
    "Cantidad": 3,
    "Disponible": True
}
```

Como se observa en el código de arriba, el objeto `verduleria` es un diccionario con tres elementos. Estos últimos, a diferencia de las listas y las tuplas, se definen con un par de objetos separados mediante el símbolo "`:`". Al lado izquierdo de éste se encuentra la **clave** y, a la derecha, el **valor**.

De este modo, todo diccionario se compone de elementos que son **pares clave-valor**. En Python, estos también reciben el nombre de **ítems**.

Es importante tener en cuenta los siguientes aspectos al trabajar con diccionarios:

1. Las **claves** (*keys*) deben **ser únicas** entre sí. Es decir, no se pueden repetir.

2. Solo es posible usar tipos de datos **inmutables** para definir una clave. Por ejemplo, valores numéricos (`int` o `float`), cadenas de texto (`str`) o tuplas (`tuple`), pero no listas (`list`).

3. Los ítems de un diccionario **no están vinculados a un índice**, como ocurre con las listas o las tuplas.

4. Se puede usar la función `len()` en diccionarios para saber cuántos ítems hay en ellos.

Observemos, a modo de ejemplo, el punto 3 para ver cómo se accede a los elementos de un diccionario que llamaremos `dict_01`.

```python
dict_01 = {
  1: "hola",
  (3, "m"): 5.1,
  "Seguir": True
}
```

Como se mencionó anteriormente, los ítems de un diccionario no están vinculados a un índice, por lo que no es posible acceder a ellos escribiendo dichos números adentro de "`[ ]`". Para lograr ese objetivo, se usan sus **claves** en dichos paréntesis, como se observa a continuación:

```
>>> print(dict_01["Seguir"])
True
>>> print(dict_01[(3, "m")])
5.1
```


## 6.4 Funciones y métodos en diccionarios.

Luego de definir un diccionario, es posible aplicar distintos métodos y funciones para manipular o explorar sus ítems. Algunos son exclusivos de aquella estructura de datos, pero no todos lo son (por ejemplo, `len()`). Ahora se revisará un subconjunto de ellos. El resto pueden ser encontrados en la [documentación oficial de Python](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict).

Volvamos a usar el siguiente diccionario:

```python
verduleria = {
    "Fruta": "Manzana",
    "Cantidad": 3,
    "Disponible": True
}
```

En la sección 6.3 vimos que podemos acceder al valor de un ítem de un diccionario escribiendo su correspondiente clave adentro de un paréntesis "`[ ]`". Si queremos obtenerlos todos, una manera sería hacerlo secuencialmente mediante un búcle `for` tal como se ve a continuación:

```python
for clave in ["Fruta", "Cantidad", "Disponible"]:
    print(verduleria[clave])
```

Sin embargo, obtener los valores de los ítems de `verduleria` de esa manera sería tedioso si, en vez de ser solo tres, fueran miles. Afortunadamente, los métodos `.keys()` y `.values()` pueden facilitar esa tarea, como se aprecia abajo:

```python
# Usando el metodo `.keys()`
for clave in verduleria.keys():
    print(verduleria[clave])

# Usando el metodo `.values()`
for valor in verduleria.values():
    print(valor)
```

En ambos búcles `for` del código de arriba se obtiene el mismo resultado:

```
Manzana
3
True
```

El método `.keys()` entrega las **claves** de un diccionario, mientras que `.values()` los **valores** de la misma estructura de datos.

```
>>> verduleria.keys()
dict_keys(['Fruta', 'Cantidad', 'Disponible'])
>>> verduleria.values()
dict_values(['Manzana', 3, True])
```

En Python, los objetos `dict_values(['Manzana', 3, True)` o `dict_keys(['Fruta', 'Cantidad', 'Disponible'])` se conocen como **vistas** o ***views*** y se caracterizan por ser **iterables**. Es decir, pueden ser leídos secuencialmente por búcles como el `for`.

En la sección anterior se señaló que los diccionarios son **mutables**. Para modificar un valor, simplemente usamos su clave como índice y asignamos su nuevo valor.

```
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 3, 'Disponible': True}
>>> verduleria["Cantidad"] = 1 # Item "Cantidad" actualizado
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 1, 'Disponible': True}
```

Ahora suponga que quiere **añadir un nuevo ítem a su diccionario**. Existen dos maneras. Una de ellas es usando la técnica `dict[nueva_clave] = nuevo_valor`, como se observa a continuación:

```
>>> verduleria["Color"] = "Rojo"
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 1, 'Disponible': True, 'Color': 'Rojo'}
```

La otra es forma de agregar un nuevo ítem en un diccionario es mediante el método `.update()`. Por ejemplo, añadamos el ítem `"Exportable": False` a `verduleria`.

```
>>> verduleria.update(Exportable = False)
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 1, 'Disponible': True, 'Color': 'Rojo', 'Exportable': False}
```

Una ventaja adicional del método `.update()` es que permite agregar de una sola vez **múltiples ítems** en un mismo diccionario.

Con el método `.update()` también es posible **modificar el valor de un ítem**. Usémoslo para reestablecer el valor de la clave `"Cantidad"` a `3` en el diccionario `verduleria`.

```
>>> verduleria.update(Cantidad = 3)
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 3, 'Disponible': True, 'Color': 'Rojo', 'Exportable': False}
```

Finalmente, para eliminar un ítem de un diccionario se puede lograr a partir de la *keyword* `del`, indicando su **clave**.

```
>>> del verduleria["Exportable"]
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 3, 'Disponible': True, 'Color': 'Rojo'}
```

Otras formas para quitar ítems de un diccionario son por medio de los métodos `.pop()` o `.popitem()`. En el primero, se debe indicar la **clave** para que lo elimine en dicha posición, mientras que **el segundo elimina automáticamente el último ítem**.

```
>>> verduleria.pop("Disponible")
True
>>> verduleria.popitem()
('Color', 'Rojo')
>>> print(verduleria)
{'Fruta': 'Manzana', 'Cantidad': 3}
```


