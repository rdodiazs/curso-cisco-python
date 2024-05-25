# 2. Búcles en Python.

## 2.8 Declaraciones `break` y `continue`.

Cuando en un programa existen estructuras de repetición (o iteración), como los `while` o los `for`, muchas veces vamos a querer, bajo ciertas condiciones, interrumpir sus bloques de código. Para ello, Python ofrece las palabras claves (*keywords*) `break` y `continue`.

1. **`break`**: Termina inmediatamente el búcle de un programa y este sigue ejecutándose en la línea posterior al bloque de código de esta iteración.

2. **`continue`**: Cuando es alcanzado, el programa ejecuta la siguiente iteración del bucle, independiente si aún existen instrucciones en el bloque de esta estructura de control.

A continuación vemos un ejemplo con la *keyword* `continue` en un bucle `for`.

```python
for i in range(0, 6):
    if i == 3:
         print("Ha llegado a la mitad del rango")
         continue
    print(i)
```

Al ejecutar este código, se obtiene lo siguiente:

```
0
1
2
Ha llegado a la mitad del rango
4
5
```

Ahora observamos otro ejemplo en un bucle `while` usando la *keyword* `break`.

```python
i = 0
while i < 6:
    if i == 3:
        print(f"Como i = {i}, este programa se termina")
        break
    print(i)
    i += 1
```

El ejemplo de arriba resulta en lo siguiente:

```
0
1
2
Como i = 3, este programa se termina
```

