# 1. El programa "¡Hola, mundo!".

## 1.2 Función `print()`.

En programación, las funciones son una **parte separada del código** capaz de: 

- Causar un efecto: Por ejemplo, enviar texto a la consola, crear un archivo, etc.
- Evaluar un valor y regresarlo como el resultado de una función.

La primera característica de una función la aleja de las estudiadas en matemáticas, mientras que la segunda la asemeja más. Aún así, ambas "funciones" son distintas.

La función `print()` es un ejemplo clásico en Python de una función en programación. En este lenguaje, devuelve una cadena de texto (o salida) a la pantalla, terminal o consola (según lo que se esté usando para ejecutar el código).

```
>> print("Hola")
Hola
```

En Python, las funciones pueden venir de:

- Python mismo: En este lenguaje vienen distintas funciones integradas (o previamente creadas). Un ejemplo es `print()`.
- Módulos: Estos pueden ser entendido como extensiones de Python. En ellos, se encuentran funciones desarrolladas.
- Nuestro archivo fuente: Uno mismo puede escribir sus propias funciones.

Si uno crea sus propias funciones, siempre se recomienda nombrarlas según lo que realicen. Por ejemplo, `print()` es un buen caso porque "imprime" (*print*) texto en la pantalla.


## 1.3 Argumento de las funciones.

Además de generar generar un efecto y entregrar un resultado, otro elemento que compone a las funciones en programación son sus **argumentos**.

Al igual que sus símiles en matemática, las funciones en programación pueden tener definida una cantidad determinada de argumentos, pero también es posible que no tengan alguno. Este número solo depende de las necesidades del usuario que las utilizará.

En Python, toda función siempre debe ser ejecutada con un par de paréntesis `()` posterior a su nombre, independiente de que deba indicarse argumentos o no. En el primer caso, estos deben ir al interior del paréntesis.

Por ejemplo, la función `print()` solo puede ser ejecutada con los paréntesis a la derecha de la palabra `print`. Su principal argumento es solicitar una cadena de caracter, pero puede ser invocada sin añadir nada adentro de sus paréntesis.

La **invocación de una función** se refiere a cuando su nombre es ejecutada en el interpretador con su par de paréntesis incluido.


## 1.6 La función `print()`: Sus efectos, argumentos y valores de retorno.

A continuación se resumen los efectos, argumentos y valores de retorno de la función `print()`:

- **Efecto**: Luego de tomar los argumentos que uno incluyó en la función, los convierte en forma legible para personas para, finalmente, enviar los datos resultantes al dispositivo de pantalla (probablemente, a la consola).

- **Argumentos**: Esta función puede esperar cualquier argumento, incluido ninguno.

- **Valores de retorno**: Ninguno, solo su efecto es suficiente.


## 1.7 Instrucciones.

Cada comando que es escrito en un archivo fuente, corresponde a una **instrucción**. Un ejemplo de esta fue la "invocación de una función" (`print()`).

En Python, cada línea del código fuente puede ejecutar:

- Ninguna instrucción
- Una instrucción.

Es decir, en Python **no está permitido** ejecutar **dos o más instrucciones en una misma línea de código**.

Algo que se debe tener en cuenta, es que Python ejecuta las instrucciones **en el orden descendente** en que fueron escritas en el código fuente. Veamos el siguiente ejemplo:

```python
print("hola")
print("¿cómo estás?")
print("adiós")
```

Al ejecutar el código de arriba, veremos que su efecto será mostrado en la consola en orden descendente:

```
hola
¿cómo estás?
adiós
```

Es decir, la cadena "adiós" no saldrá antes de "¿cómo estás?" ni menos de "hola".


## 1.8 Caracter de escape y caracter de línea nueva.

Al interior de una cadena de caracteres, es posible cambiar el comportamiento de algunos caracteres. Esto es posible al añadir un *backslash* `\` al lado izquierdo de ellos, el cual recibe el nombre de **caracter de escape**.

Un caso de la aplicación del caracter de escape es cuando queremos agregar una **línea nueva** luego de haber escrito, por ejemplo, una palabra adentro de una cadena de caracteres. Esta se conoce como **caracter de línea nueva** y se logra al escribir el caracter de escape `\` antes del caracter `n`. A continuación vemos un ejemplo:

```python
print("Hola, humano.\nBienvenido")
```

Al ejecutar la función `print()` vista en el código de arriba, en la consola veremos lo siguiente:

```
>>> print("Hola, humano.\nBienvenido")
Hola, humano
Bienvenido
```

Debido a que el caracter de escape `\` cumple su función adentro de una cadena de caracteres, si queremos que no lo haga, simplemente escribimos `\\`. En ese caso, en la consola solo aparecerá el caracter `\`.


## 1.10 Argumentos posicionales.

Una función en Python puede tener argumentos que serán ejecutados según el orden dónde hayan sido ubicados. Estos reciben el nombre de **argumentos posicionales**. Veamos el siguiente ejemplo con la función `print()`.

```python
print("hola", "cien", "mañana")
```

En el ejemplo de arriba, los argumentos de `print()` son posicionales, porque al ejecutar esta función veremos que cada uno aparecerá en pantalla en el orden en que fueron ubicados arriba.

```
>>> print("hola", "cien", "mañana")
hola cien mañana
```

Como vemos, `"hola"` aparece más a la izquierda porque fue el primer argumento de `print()` y así mismo con los demás.


## 1.11 Argumentos de palabra clave (*keyword*).

Otro tipo de argumentos que es posible encontrar en funciones de Python se conocen como **argumentos de palabra clave** o *keyword arguments* en inglés. Son aquellos que **se asignan a una palabra especial**.

Por ejemplo, en la función `print()` tiene un argumento llamado `end` y es del tipo palabra clave. A continuación lo usamos:

```python
print("hola", end = " ")
print("humano")
```

Lo que hace el argumento `end` en `print("hola", end = " ")` es que todo caracter que se ejecute posterior a dicha función, será unido a su derecha en vez de aparecer en la siguiente línea.

```
hola humano
```

Sin el argumento de palabra clave `end` en `print()`, el código de arriba aparecerá en la consola como:

```
hola
humano
```

Por lo tanto, la principal diferencia entre los argumentos de palabra clave de los de posición es que los primeros tienen asignados una palabra especial, pero no se ejecutarán en la función según el orden donde hayan sido asignados.


