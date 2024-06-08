# 4. Alcances (*scopes*) en Python.

## 4.1 Funciones y alcances.

En términos generales, el **alcance de un nombre** (sea el de una variable, una función, etc) es la parte de un programa donde puede ser reconocido por el interpretador.

Por ejemplo, si definimos el **nombre de una variable adentro de una función**, su alcance solo será en el cuerpo de ésta. Si la intentamos ejecutar afuera de ella se generará un error debido a dónde fue definida.

```python
def funcion_01():
    x = "hola"
    return x

print(x)
```

```
>>> print(x)
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

Por otra parte, **si una variable es definida afuera de una función**, su alcance será tanto afuera como adentro de esta última. Veamos el siguiente ejemplo:

```python
x = "abc"

def funcion_01():
    return x

print(x)
funcion_01()
```

Al ejecutar `print(x)` y luego `funcion_01()`, se obtiene lo siguiente:

```
abc
'abc'
```

El primer `abc` corresponde al de `print(x)`, mientras que el segundo proviene de `funcion_01()`.


## 4.2 La palabra clave *global*.

Observemos el siguiente código:

```python
x = "abc"

def funcion_01():
    x = "hola"
    return x

funcion_01()
print(x)
```

Al ejecutar este código, se obtiene lo siguiente:

```
>>> funcion_01()
'hola'
>>> print(x)
abc
```

En otras palabras, `funcion_01()` **no modificó** a la variable `x` que fue definida antes de ella, siendo que dicho nombre fue usado también en el cuerpo de esa función. Para lograr esta tarea, podemos usar la palabra clave (*keyword*) ***global***.

Volvamos al código visto anteriormente, pero ahora definiendo a `x` como `global` adentro de `funcion_01()`.

```python
x = "abc"

def funcion_01():
    global x
    x = "hola"
    return x

funcion_01()
print(x)
```

Observemos lo que ocurre al ejecutar `funcion_01()` y, luego, `print(x):

```
>>> funcion_01()
'hola'
>>> print(x)
hola
```

Como se puede apreciar arriba, luego de ejecutar `funcion_01()`, la variable `x` fue modificada a la que estaba adentro de dicha función. Lo anterior se debe a que, al usar la palabra clave `global` en ella, su alcance pasó a ser **global**. Es decir, forzamos a que Python asumiera **como si esta hubiera sido definida afuera de la función**.

En ese sentido, cuando una variable es definida adentro de una función, se dice que su alcance es **Local**.
