# 1. Funciones.

## 1.2 Razones para usar funciones.

En Python, una función es definida de la siguiente manera:

```python
def nombre_funcion():
    pieza de código
```

Como se observa en el código de arriba, para crear funciones debemos usar la *keyword* **`def`** antes de nombrarla. Además, al lado derecho de su nombre, debe ir un paréntesis (`nombre_funcion()`) y, adentro de este último, se pueden establecer sus argumentos, aunque es posible que no tenga alguno.

En general, se pueden considerar dos motivos para crear y usar funciones:

1. Cuando una misma pieza de código se repite en varias partes del código fuente.

2. Cuando el código fuente va creciendo mucho.

En el primer caso, es mucho más recomendado crear una función para esa pieza de código que se va repitiendo mucho, porque después es más fácil de mantenerla.

Para el segundo motivo, es recomendado usar funciones para comenzar a separar el código fuente en archivos fuentes más pequeños y, para las instrucciones que se repitan, se pueden usar funciones. Esta técnica también se conoce como **descomposición**.


## 1.5 Cómo opera una función.

Para entender cómo opera una función, veamos el siguiente código:

```python
def funcion_01():
    print("Mensaje en la mitad")

print("Mensaje al inicio")
funcion_01()
print("Mensaje al final")
```

Al inicio del código de arriba, definimos la función `funcion_01()`. Al hacerlo, Python se encarga de recordar (o almancenar en la memoria) dónde se hizo aquello. Luego, al invocarla (que es cuando escribimos su nombre junto con sus paréntesis), el lenguaje vuelve a donde se definió `funcion_01()`, ejecuta el **cuerpo de la función** (es decir, `print("Mensaje de la mitad")`) para, finalmente, volver (*return*) a donde fue invocada y continua con la siguiente línea de código, que corresponde a la instrucción `print("Mensaje al final")`.

