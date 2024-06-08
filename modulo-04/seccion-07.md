# 7. Excepciones.

## 7.3 Las ramas  `try - except`.

Suponga que creamos el siguiente programa en Python que será ejecutado por otra persona, que llamaremos como usuario:

```python
numero = int(input("Ingrese un número natural: "))
print("El recíproco de " + str(numero) + " es " + "1/" + str(numero) + " = " + str(1/numero))
```

Si el usuario ingresa el número `2`, entonces obtendrá el mensaje que se muestra a continuación:

```
El recíproco de 2 es 1/2 = 0.5
```

Ahora, si el mismo usuario u otra persona vuelve a ejecutar el programa de arriba e ingresa la letra `a`, el programa se terminará y obtendrá el siguiente mensaje de error:

```
Traceback (most recent call last):
  ...
    numero = int(input("Ingrese un número natural: "))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'a'
```

La última línea del mensaje de error de arriba es la que más interesa. Señala que se ha incurrido en un **error de valor**, cuya palabra clave es `ValueError`, puesto que se ha ingresado un literal inválido para la función `int()`: la letra `a`.

Frente a este tipo de situaciones nos enfrentaremos a dos desafíos:

1. Evitar que el usuario ingrese un dato que no corresponde al propósito del programa.

2. Si sucede el error, que se muestre su mensaje, pero sin que el programa se termine de inmediato.

Las palabras claves `try` y `except` son las que pueden brindar ayuda en ambos desafíos. Son ramas de control de flujo (como los `if`, `else` y `elif`), pero tienen como propósito **evaluar y manejar errores de programación**. A continuación se muestra su sintáxis:

```python
try:
    # Donde se evalúa la ocurrencia de un error esperado
except:
    # El código que se ejecutará si sucede el error evaluado en el `try`
```

Cuando sucede el error evaluado en el código del `try`, este recibe el nombre de **excepción**. Por otra parte, cuando ocurre la excepción, dicho proceso se conoce como **surgimiento** (***rising***).

Añadamos el programa que escribimos anteriormente en una rama `try - except`.

```python
try:
    numero = int(input("Ingrese un número natural: "))
    print("El recíproco de " + str(numero) + " es " + "1/" + str(numero) + " = " + str(1/numero))
except:
    print("Debes ingresar un número natural")

print("El programa siguió ejecutándose")
```

Como se aprecia en el código de arriba, se agregó al final de éste la función `print()` con el mensaje `"El programa siguió ejecutándose"` para demostrar que, aunque suceda el error, el programa no terminará. Al probar esta afirmación ingresando la letra `a` al correr este código, se obtiene el siguiente mensaje:

```
Ingrese un número natural: a
Debes ingresar un número natural
El programa siguió ejecutándose
```

Si bien el programa que se está desarrollando cumple con mostrar un error sin que deje de ejecutarse, Python aún "no sabe" cuál fue exactamente. En este lenguaje existen *keywords* para ayudar a que el interpretador se dirija a la excepción correspondiente a ese error. Para este caso, se usará el de `ValueError` de la siguiente forma:

```python
try:
    numero = int(input("Ingrese un número natural: "))
    print("El recíproco de " + str(numero) + " es " + "1/" + str(numero) + " = " + str(1/numero))
except ValueError:
    print("Debes ingresar un número natural")

print("El programa siguió ejecutándose")
```

Se ha usado la palabra clave `ValueError` en el `except` del código de arriba porque ese es el error que se está evaluando: Que el usuario ingrese un dato que no es un número entero.

Existen más palabras claves como `ValueError` para trabajar con errores en Python. Estas se abordarán más adelante.


## 7.5 Dos excepciones después de un `try`.

Volvamos al programa con el que hemos trabajado en esta sección:

```python
try:
    numero = int(input("Ingrese un número natural: "))
    print("El recíproco de " + str(numero) + " es " + "1/" + str(numero) + " = " + str(1/numero))
except ValueError:
    print("Debes ingresar un número natural")

print("El programa siguió ejecutándose")
```

Otro error que puede cometer un usuario en el programa de arriba, es que ingrese el número `0`. Al igual que en la sección  7.3, se puede evitar que el programa lo informe sin que termine al establecer el `except` como `ZeroDivisionError`, pero ya lo tenemos definido como `ValueError`. En estos casos, lo recomendado es **añadir un nuevo `except`**, tal como se observa a continuación:

```python
try:
    numero = int(input("Ingrese un número natural: "))
    print("El recíproco de " + str(numero) + " es " + "1/" + str(numero) + " = " + str(1/numero))
except ValueError:
    print("Debes ingresar un número natural")
except ZeroDivisionError:
    print("Estás dividiendo por cero")

print("El programa siguió ejecutándose")
```

Al ejecutarlo y, luego, al ingresar el valor `0`, se obtienen los mensajes de a continuación:

```
Estás dividiendo por cero      
El programa siguió ejecutándose
```

Como se aprecia arriba, el programa manda el mensaje de error que se le instruyó y no termina inmediatamente.

En Python se pueden agregar la cantidad de excepciones que uno quiera. Todo dependerá del programa que se esté desarrollando.


## 7.7  Algunas excepciones útiles.

Al final de la sección 7.3 se mencionó que se profundizarán algunas palabras claves que pueden ser usadas en ramas de `except`. Ahora serán abordadas.

### 7.7.1 ZeroErrorDivision.

El error llamado `ZeroErrorDivision` aparece cuando uno intenta forzar una división por cero, sea que uno ingrese ese valor o que lo haga con uno extremadamente cercano a este.

### 7.7.2 ValueError.

Esta excepción surge cuando se intenta trabajar con valores que son inapropiados para un contexto determinado. Por ejemplo, al escribir `int("1ab")`.

### 7.7.3 TypeError.

Sucede cuando se intenta aplicar un dato en un contexto donde no corresponde.

### 7.7.4 AttributeError.

Se activa en el momento en que se intenta invocar un método que no existe para el ítem en que se está aplicando. Un ejemplo es al ejecutar `(1, 2, 4).append(3)`.

### 7.7.5 SyntaxError.

Este tipo de error surge cuando, en una línea de código, se viola la gramática de Python. Un caso puede ser al invocar la función `print()` como `pirnt()`.

