# 6. Interacción con el usuario.

## 6.1 Función `input()`.

En las secciones anteriores se ha usado la función `print()` para mostrar datos en la consola con la que interactúa el usuario. En otras palabras, cumple la tarea de **salida** (*output*) en un programa computacional. En Python también existe una función para la **entrada** (*input*) de datos llamada `input()`.

Específicamente, la función `input()` lee los datos ingresados por un usuario y, luego, lo regresa mientras se ejecuta el programa.

Algo a tener en cuenta con `input()` es que el valor entregado es de tipo `string`.


A continuación vemos dos maneras de usar la función `input()`. La primera es sin argumento:

```python
print("Ingrese su nombre: ")
nombre = input()

print("Bienvenido a casa,", nombre)
```

Al ejecutar el código, veremos que se ejecutará de la siguiente manera:

```
Ingrese su nombre: 
_
```

El `_` corresponde al cursor de la consola que espera a que ingresemos, en este caso, nuestro nombre. Al hacerlo, el resultado será parecido a lo que vemos a continuación:

```
Ingrese su nombre: 
Joe
Bienvenido a casa, Joe
```

Una forma más corta de escribir este mensaje, es escribir la cadena `"Ingrese su nombre: "` como **argumento de la función** `input()`, en vez de ingresarlo en `print()`.

```python
nombre = input("Ingrese su nombre: ")
print("Bienvenido a casa, ", nombre)
```

El resultado del código de arriba será como se observa a continuación:

```
Ingrese su nombre: Joe
Bienvenido a casa, Joe
```


## 6.5 Conversión de tipo de dato (*type casting*).

En Python existen funciones para convertir el tipo de dato de una variable a otra. A continuación se presentan algunas de las más usadas:

- `int()`: Convierte un número o cadena de caracteres a entero (`int`).
- `float()`: Devuelve un valor punto-flotante (`float`) de un número o cadena.
- `str()`: Transforma cualquier objeto a uno de tipo cadena (`str`).

Es posible verificar el tipo de dato, tanto para un literal como para una variable, mediante la función  `type()`. Por ejemplo, al ejecutar

```python
palabra = "hola"
type(palabra)
```

Obtendremos como resultado:

```
<class 'str'>
```


## 6.7 Operadores para cadenas de caracteres.

Al trabajar con cadenas de caracteres, es posible utilizar dos operadores binarios: `+` y `*`.

El operador `+` sirve para **concatenar** o unir dos cadenas de caracteres que se ubican a su izquierda y derecha.

```python
bienvenida = "Bienvenido a casa, "
nombre = "Joe"
saludo = bienvenida + nombre

print(saludo)
```

Al ejecutar el comando `print(saludo)`, obtendremos en la pantalla la unión de las cadenas `bienvenida` y `nombre`.

``` 
Bienvenido a casa, Joe
```

Por otra parte, el operador `*` es utilizado para **replicar** una cadena de caracter una o más veces. Funciona escribiendo la cadena a su izquierda, mientras que en la derecha va un número entero que indica cuántas veces queremos que se repita la cadena.

```
>>> print("hola" * 5)
holaholaholaholahola
```
