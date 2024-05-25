# 1. Tomando decisiones en Python.

## 1.5 Utilizando nuestras respuestas.

Si usamos operadores lógicos (`>`, `<`, `>=`, `<=`, `==` o `!=`) para evaluar dos valores o expresiones, obtendremos uno de los dos valores booleanos `True` o `False`. Por ejemplo,

```
>>> 2 == 1
False
```

Ante el resultado visto arriba, podemos preguntarnos qué es lo que podemos hacer con éste. Una opción es guardarlo en una variable.

```
>>> var = 2 == 1
>>> var
False
```

Otra opción es usar el resultado de `2 == 1` para **evaluar a futuro otra expresión**. Principalmente, para decidir ejecutar un bloque de código de una declaración `if - else` o `elif`.

Los valores booleanos `True` y `False` equivalen a los números `1` y `0`, respectivamente.

```
>>> int(True)
1
>>> int(False)
0
```

Por otra parte, debemos tener en consideración que las operaciones lógicas tienen un **nivel de prioridad más bajo** que las operaciones binarias y unarias vistas en la [sección 3 del módulo 2](..\modulo-02\seccion-03.md). Ilustremos este punto en el siguiente ejemplo:

```
>>> 2 > 1 * 5
False
```

El resultado de `2 > 1 * 5` es `False` porque la operación que tiene mayor prioridad en Python es la de multiplicación `*`. Por lo tanto, es la primera que se realiza. En cambio, `>` tiene una prioridad más baja, implicando que se realizará después de `*`. Así, este lenguaje hizo el siguiente trabajo:

1. Calcula `1 * 5`, que es igual a `5`.
2. Compara si `2 > 5`.
3. Entrega el resultado de `2 > 5`, que es `False`.

Otra manera de explicar el ejemplo `2 > 1 * 5`, es que Python lo considera como `2 > (1 * 5)`. Independiente de la operación, este lenguaje de programación siempre le dará prioridad a lo que está en paréntesis.

A continuación actualizamos la tabla sobre el orden de prioridad que tienen las operaciones en Python, vista en el módulo 2.

|Prioridad |            Nombre                |       Símbolo       |   Tipo   |
|:--------:|:--------------------------------:|:-------------------:|:--------:|
|     1    |         Exponenciación           |         `**`        | Binario  |
|     2    |      Positivo y negativo         |       `+` y `-`     | Unarios  |
|     3    |  Mult, divisiones y módulo       | `*`, `/`, `//` y `%`| Binarios |
|     4    |          Suma y resta            |       `+` y `-`     | Binarios |
|     5    | Menor (o igual) y mayor (o igual)| `<`, `<=`, `>`, `>=`| Binarios | 
|     6    |    Igual que y distinto que      |      `==` y `!=`    | Binarios |

