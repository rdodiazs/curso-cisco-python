# 2. Forma en que las funciones se comunican con su entorno.

## 2.1 Funciones parametrizadas.

En la sección 1 de este módulo, se señaló que una función puede tener argumentos adentro de su paréntesis como no tenerlos. Para el primer caso, definimos **parámetros**.

Un **parámetro**  es una variable que es ejecutada solo en y para el **cuerpo de la función** donde es definida. Esto implica que afuera de una función, el parámetro no existe.

Habiendo definido lo que es un parámetro, debemos diferenciarlo de un **argumento**. Este últmo corresponde **al valor que uno le asigna a un parámetro**. Veamos el siguiente ejemplo para entender mejor esta comparación:

```python
def adicion(a, b):
    suma = a + b
    print(str(a) + " + " + str(b) + " = " + str(suma))

adicion(1, 2)
```

Los parámetros corresponden a las letras `a` y `b`, que son escritas al definir la función `adicion()`. En cambio, sus argumentos son los enteros `1` y `2`, respectivamente.


## 2.2 Parámetros posicionales.

En Python, los parámetros de una función se clasifican en dos tipos:

1. Posicionales.
2. Palabra clave (*keywords*).

Los **parámetros posicionales** son todos aquellos que son definidos en el cuerpo de una función y que son ejecutados en el orden en que fueron nombrados adentro del paréntesis ubicado a la derecha de su nombre.

Volvamos al ejemplo que vimos en la sección 2.1:

```python
def adicion(a, b):
    suma = a + b
    print(str(a) + " + " + str(b) + " = " + str(suma))

adicion(1, 2)
```

En la función `adicion()`, `a` y `b` son sus parámetros posicionales, donde `a` es el primer parámetro posicional y `b` el segundo. Al ejecutar `adicion(1, 2)`, Python tomará primero a `1` (**primer argumento posicional**) y luego a `2` (**segundo argumento posicional**) para, posteriormente, invocarla.


## 2.3 Parámetros de palabra clave.

Un segundo tipo de parámetros que existen en Python son los de **palabra clave**, que en inglés se conocen como ***keywords parameters***.

Básicamente, los parámetros de palabra clave son aquellos que se definen al mencionarlos adentro del paréntesis de una función cuando está siendo invocada. Por ejemplo, en el siguiente código:

```python
def adicion(a, b):
    suma = a + b
    print(str(a) + " + " + str(b) + " = " + str(suma))

adicion(a = 1, b = 2)
```

cuando se invoca la función `adicion` como `adicion(a = 1, b = 2)`, los parámetros `a` y `b` están siendo tratados como de **palabras claves**. Los valores `1` y `2` reciben el nombre de **argumentos de palabra clave**.

Una acotación que merece ser mencionada, es que en documentaciones de Python, los **argumentos de palabra clave** suelen ser abreviadas como ***kargs***, que provienen de la frase en inglés ***keyword arguments***.


## 2.4 Combinando argumentos posicionales y de palabra clave.

A partir de lo estudiado en las secciones 2.3 y 2.4, el tipo de parámetro se establecerá según cómo designemos sus argumentos. En ese sentido, es posible definirlos de manera combinada para invocar una función. No obstante, en Python se debe cumplir con una sola regla: **Los argumentos posicionales siempre deben ser definidos antes que los de palabra clave**.

Veamos el siguiente ejemplo:

```python
def adicion(a, b):
    suma = a + b
    print(str(a) + " + " + str(b) + " = " + str(suma))

adicion(a = 1, 2)
```

Si ejecutamos el código de arriba, obtendremos un mensaje de error desde el interpretador de Python.

```
    adicion(a = 1, 2)
                    ^
SyntaxError: positional argument follows keyword argument
```

Como se puede apreciar en el mensaje de error, se refiere a que definimos el primer argumento como de palabra clave (*keyword*) cuando debería ser uno posicional.


