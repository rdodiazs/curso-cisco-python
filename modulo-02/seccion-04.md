# 4. Variables

## 4.1 Variables: Datos en forma de caja.

Cuando realizamos operaciones aritméticas entre literales, es muy posible que queramos almacenar dichos resultados para utilizarlos más tarde. Aquellos "contenedores" de datos se llaman **variables**.

Una variable puede ser entendida como una caja: Almacena información (dato) bajo un nombre que lo identifique. Para ser más específico, es almacenado en una porción de memoria (RAM).

Toda variable en Python consiste de:

- Un nombre.
- Un valor.

Es uno, como desarrollador, el que debe crearlas y la cantidad que existirán en un programa también depende de nosotros.


## 4.2 Nombre de variables.

Para nombrar una variable en Python, debemos seguir las siguientes **reglas**:

1. Solo puede estar compuesta de letras mayúsculas y minúsculas, dígitos y el caracter `_` (guión bajo).
2. Siempre debe comenzar con una letra (el guión bajo también es tratado como una letra).
3. Las letras mayúsculas y minúsculas son tratadas como **distintas** (por ejemplo, "A" no es lo mismo que "a").
4. Se prohibe el uso de palabras reservadas por Python (también conocidas como **keywords** o **palabras claves**).

No hay restricción en el largo del nombre de una variable.

Algunas palabras claves, reservadas en Python, son:

```
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```


## 4.8 Operadores de atajo.

Suponga que tenemos dos variables definidas `x` y `ovejas`. También, que las hemos redefinido para que realicen las siguientes operaciones:

```
x = x * 2

ovejas = ovejas + 1
```

En Python, es posible reducir la escritura de ambas operaciones escritas en el código de arriba como se observa a continuación:

```
x *= 2

ovejas += 1
```

Tanto `*=` como `+=` reciben el nombre de **operadores de atajo**. También son aplicables para el resto de las **operaciones binarias** (es decir, para la resta, división [entera y flotante], exponenciación y módulo).

