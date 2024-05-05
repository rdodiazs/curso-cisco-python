# 5. Comentarios.

## 5.1 Comentarios: Por qué, cuándo y cómo.

Cuando escribamos código en un archivo fuente, no siempre recordaremos qué es lo que se ejecuta en cada línea o pieza de código. También puede darse una situación similar si lo compartimos con otra persona. Para reducir ese trabajo de decifrar "qué es lo que hace", usamos **comentarios**.

Para escribir un comentario en Python, usamos el símbolo `#`. Su función es que indica al interpretador que la línea donde se encuentre, no debe ser leída o ejecutada. Por ejemplo:

```python
# Las siguientes lineas calculan la suma de dos numeros, `a` y `b`.
# El resultado de la suma se almacena en la variable `c`
a = 1
b = 2
c = a + b
```

En ese sentido, también puede ser usada para que no se ejecute un comando, como vemos a continuación:

```python
# No ejecutar la siguiente línea.
# print("Hola")

# Ejecutar la de acontinuación
print("¿Cómo estás?")
```

