# 3. Devolviendo el resultado de una función.

## 3.1 Efectos y resultados: La instrucción `return`.

Al invocar una función, comúnmente uno va a querer obtener de vuelta el resultado de lo que se realizó en el código de su cuerpo. En la sección 2 usamos la función `print()` para esa tarea. Por ejemplo,

```python
def bienvenido(nombre):
  saludo = "Bienvenido, " + nombre + "!"
  print(saludo)
```

Pero qué ocurre si, luego de que una función devuelva su resultado, queremos que termine inmediatamente el código de su cuerpo y vuelva al lugar donde fue invocada. Aquello no lo podemos realizar con la función `print()`. Veamos el ejemplo de a continuación:

```python
def bienvenido(nombre, con_saludo = True):
  if con_saludo == False:
    print("Adios")
  
  saludo = "Bienvenido, " + nombre + "!"
  print(saludo) 
```

Si ejecutamos el código de arriba estableciendo el parámetro `con_saludo = False` en `bienvenido()`, se obtiene lo siguiente:

```
>>> bienvenido("John", con_saludo = False)
Adios
Bienvenido, John!
```

El problema del resultado que se obtuvo con `bienvenido()` es que, aunque no queríamos que devolviera el saludo, lo hizo igual. Eso se debe a que la función `print()` no previene aquello.

Para las funciones, en Python existe una palabra clave que permite:

1. Devolver el resultado de una función.
2. Salir de la función invocada.

Esta palabra clave corresponde a **`return`**.


Al usar `return` en una función, es posible salir de ella con o sin un resultado de salida. En los siguientes dos códigos se aplican ambas opciones:

```python
# Uso de `return` sin un valor de salida.
def bienvenido(nombre, con_saludo = True):
  if con_saludo == False:
    return
  
  saludo = "Bienvenido, " + nombre + "!"
  print(saludo)
```

```python
# Uso de `return` con un valor de salida.
def adicion(a, b):
  suma = a + b
  return suma
```

Si ejecutamos el comando `bienvenido("John", con_saludo = False)`, simplemente salimos de la función y no obtenemos un resultado. 

```
>>> bienvenido("John", con_saludo = False)
>>>
```

Por otra parte, al ejecutar `adicion(2, 3)`, esta función nos devuelve el resultado de la suma porque, a la derecha de `return`, mencionamos a la variable `suma` que almacena dicha operación.

```
>>> adicion(2, 3)
5
```

## 3.2 Breves palabras sobre `None`.

Un valor especial que existe en Python corresponde a la palabra clave `None`.

En estricto rigor, `None` **no es, en sí, un valor**, esto significa que no debemos usarlo adentro de alguna expresión. Por ejemplo, si ejecutamos el comando `print(2 + None)`, se obtiene un `TypeError` porque no es válido en Python usar el operando `+` para realizar una suma entre un dato de tipo `int` con un `None`:

```
>>> print(2 + None)
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

Se recomienda usar la palabra clave `None` para dos situaciones:

1. Para asignarlo a una variable (o usarlo como el valor de salida de una función).
2. Para comprarla con otra variable con el propósito de diagnosticar su estado interno.

