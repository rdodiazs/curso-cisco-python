# 3. Operaciones lógicas y con bits en Python.

## 3.1 Lógica computacional: Operadores `and`, `or` y `not`.

Cuando se toman decisiones en la vida real, gran parte de las veces consideramos más de una condición para realizar una tarea. Por ejemplo, nuestra condición para salir a dar un paseo es que no llueva en el día **y** que haya poco tráfico vehícular en las calles.

En programación, se intenta resolver problemas reales y, por consiguiente, cuando se establece una toma de decisión (por ejemplo, en sentencias `if - else` o `elif`), vamos a considerar una composición de decisiones para que se ejecuten bloques de códigos. Para ello, Python entrega los siguientes **operadores lógicos**:

- `and`: Conjunción lógica.
- `or`: Disjunción lógica.
- `not`: Negación lógica.

A continuación se muestra la tabla de verdad para los operadores `and` y `or`, donde `A` y `B` son dos argumentos de una expresión.

|   `A`   |    `B`   | `A and B` | `A or B` |
|:-------:|:--------:|:---------:|:--------:|
|  `True` |  `True`  |  `True`   |  `True`  |
|  `True` | `False`  |  `False`  |  `True`  |
| `False` |  `True`  |  `False`  |  `True`  |
| `False` | `False`  |  `False`  | `False`  |


Los operadores lógicos `and` y `or` se caracterizan por ser **binarios** y por tener una **prioridad menor a los de comparación** (i.e, `>`, `>=`, `<`, `<=`, `==` y `!=`). Entre ellos, `and` tiene más prioridad que `or`.

En cuanto al operador `not`, abajo se ilustra su tabla de verdad.

|    `A`   | `not A` |
|:--------:|:-------:|
|  `True`  | `False` |
|  `False` | `True`  |

El operador lógico `not` es uno de tipo **unario** y tiene más prioridad que `and` y `or`. En particular, dicho nivel es similar a los otros operadores unarios `+` y `-`.


## 3.4 Operadores bit a bit (*bitwise operators*).

Las operaciones lógicas también pueden realizarse a nivel de bit. En Python, se hacen mediante los **operadores bit a bit** (*bitwise operators*, en inglés), que corresponden a:

- `&` (ampersand): Conjunción bit a bit.
- `|` (barra): Disjunción bit a bit.
- `~` (tilde): Negación.
- `^` (intercalación): Es un `or` excluyente, también conocido como `xor`.

Como se observa en la lista de operadores bit a bit, son similares a los lógicos, pero se añade uno: El que realiza la operación `xor` a nivel de bits. Si tenemos dos argumentos `A` y `B`, la expresión `A xor B` puede entenderse como `(A and not B) or (not A and B)`.

A continuación se encuentran las tablas de verdad para las **operaciones binarias bit a bit** `&`, `|`, `^` y para la **unaria** `~`.

| `A` | `B` | `A & B` | `A | B` | `A ^ B` |
|:---:|:---:|:-------:|:-------:|:-------:|
| `1` | `1` |   `1`   |   `1`   |   `0`   |
| `1` | `0` |   `0`   |   `1`   |   `1`   |
| `0` | `1` |   `0`   |   `1`   |   `1`   |
| `0` | `0` |   `0`   |   `0`   |   `0`   |


|  `A`  | `~ A` |
|:-----:|:-----:|
|  `1`  |  `0`  |
|  `0`  |  `1`  |

Para las operaciones binarias `&`, `|` y `^`, cuando son asignadas a una variable, también es posible expresarlas de manera abreviada. En el siguiente bloque de código vemos algunos ejemplos:

```python
x &= y   # Es lo mismo que `x = x & y`
x |= y   # Es lo mismo que `x = x | y`
x ^= y   # Es lo mismo que `x = x ^ y`
```


## 3.6 Cambio binario a la izquierda y a la derecha.

Cuando realizamos las siguientes operaciones aritméticas:

```
12345 x 10 = 123450
12340 / 10 = 1234
```

lo que estamos haciendo es mover (en la multiplicación) o quitar (en la división) digitos a la derecha de la igualdad.

En Python existen operadores para cambiar los bits de un valor entero a la izquierda. Se conocen como **operadores de cambios binarios** (*shifting operators* en inglés).

Los operadores de cambios binarios **solo se aplican a valores enteros** y corresponden a los símbolos `<<` (cambio a la izquierda) y `>>` (a la derecha).

```
valor_entero << bits   # Mueven bits a la izquierda del valor entero
valor_entero >> bits   # Mueven bits a la derecha del valor entero
```

Dado que los valores binarios son potencias de base 2, las  operaciones `a << n`, mientras que `a >> n` corresponden a:

```python
a << n == a * (2**n)
a >> n == a // (2**n)  # Division entera o, en matematica, division floor.
```

