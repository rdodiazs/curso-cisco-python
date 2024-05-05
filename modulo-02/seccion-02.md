# 2. Literales de Python.

## 2.1 Literales: El dato mismo.

En Python, un literal es **un dato cuyo valor es determinado por su mismo literal**. En la [documentación oficial de este lenguaje](https://docs.python.org/3/reference/lexical_analysis.html#literals), se lo define como

> Notaciones para valores constantes de algún tipo de dato que viene predefinido en Python.

Otra manera de entender a los literales, es que corresponden al **dato crudo (*raw data*) que usamos para que sea asignado a una variable** (ya se profundizará en las variables).

En Python existen distintos tipos de literales. En el siguiente código veremos dos de ellos mediante la función `print()`.

```python
print("2")
print(2)
```

Si ejecutamos el código de arriba, obtenemos:

```
2
2
```

Como vemos, ambos `print()` entregan el mismo resultado en la consola, pero los argumentos usados son diferentes. En particular, corresponden a dos literales:

- `2` es un **literal de número entero** (*integer literal*).

- `"2"` corresponde a un **literal de cadena** (*string literal*).

Los dos literales, al ser ejecutados en el interpretador, son convertidos en código de máquina para representar lo que hemos indicado. Con la función `print()`, obtenemos como resultado sus versiones legibles para humanos.


## 2.2 Números enteros.

Los computadores modernos tratan con dos tipos de números. En general, ambos se diferencian en:

- Cómo son almacenados en la memoria (RAM) de un computador.
- El rango de valores que pueden aceptar.

La característica del valor numérico que determina su:

- Tipo (*kind*).
- Rango.
- Aplicación

se conoce como **Tipo** (*type*).

Cuando uno codifica un literal y lo añade al archivo fuente del código escrito en Python, su forma determinará cómo este lenguaje lo representará para almacenarlo en la memoria.

Uno de los tipos de números que son tratados por los computadores modernos se llaman **enteros** (*integer*) y corresponden a aquellos que **carecen de una parte fracionaria**.

La característica de los literales enteros de que carecen de una parte fraccionaria es muy relevante por lo siguiente: Independiente de la cantidad de dígitos que pueda tener una cadena de enteros, está **prohibido** usar cualquier caracter que separe a cada uno de ellos.

Por ejemplo, si escribimos `1 1` o `1..1` en Python, obtendremos un error porque no está cumpliendo con la sintáxis de este lenguaje. Por otra parte, las expresiones `1.1` o `1,1` no corresponden a enteros.

Así, tanto `1` como `11111` corresponden a literales enteros. Desde Python 3.6 en adelante, solo se acepta el uso de guiones bajos para expresar de forma alternativa a este tipo numérico. Es decir, `1111` es lo mismo que `11_11`.

### 2.2.1 Números octales y hexadecimales.

Los números enteros tienen formas alternativas de ser representados. Estos corresponden a los octales y los hexadecimales.

Un valor octal es un entero que es precedido por un `0o` (cero - o). Recibe este nombre porque dicho número solo puede contener dígitos que van del 0 al 7.

Un ejemplo puede ser `0o123`. Al ser usado como argumento de la función `print()`, nos devuelve el valor entero que representa.


```
>>> print(0o123)
83
```

Es decir, el octal `0o123` corresponde al número `83`.


Por otra parte, un valor hexadecimal es aquel entero que en su extremo izquierdo lleva un `0x` (cero - x). Por ejemplo, `0x123` es un hexadecimal que corresponde al entero `291`.

```
>>> print(0x123)
291
```


## 2.3 Números flotantes (*floats*).

El otro tipo numérico con los que tratan los computadores modernos se llama **punto-flotante** o, simplemente, números flotantes (*floats*). Son aquellos que almacenan la parte fracional, ubicada posterior a su coma (o punto) decimal.

De este modo, los valores:

```
0.4
.4
-1.5
2.0
```

son todos de tipo flotante.

Otro valor que es punto flotante, pero no lleva punto decimal, es `E` (o `e`) y es usado para expresar un valor en **notación científica**. Por ejemplo, $2 \cdot 10^{3}$ es igual a `2e3`.

En el interpretador, Python imprimirá en la pantalla la forma más "económica" de un número flotante. Por ejemplo:

```
>>> 0.0000000003
3e-10
```

La expresión `3e-10` corresponde a $3 \cdot 10^{-10}$, que es igual a `0.0000000003`. Python usa la primera para mostrar en pantalla, porque usa menos espacio.

## 2.4 Cadenas de texto (*strings*).

Como ya sabemos, las cadenas de texto son aquellos literales con caracteres encerrados entre comillas (`" "`) o comillas simples (`' '`), también llamadas apóstrofes.

Un desafío común es cuando queremos que las comillas aparezcan adentro de una cadena de caracter. Hay dos formas de solucionar aquello:

1. **Usar el caracter de escape** `\`: Por ejemplo, `"Una persona me dijo \"Hola\""` resultará en `Una persona me dijo "hola"`.

2. **Usar comillas simples al inicio**: Ejemplo: `'Una persona me dijo "Hola"'`. También saldrá en pantalla con `print()` como `Una persona me dijo "hola"`.

## 2.5 Valores Booleanos.

Un último literal que existe en Python son los **booleanos**. Son usados para evaluar la veracidad o falsedad de alguna condición que queramos evaluar. De este modo, consiste de dos valores: `True` (verdadero) o `False` (falso).

La palabra "booleano" (*boolean*) viene del matemático y lógico inglés George Boole. Destacó, entre otras cosas, por comenzar a desarrollar un área del álgebra que terminó siendo llamada "álgebra booleana", que es donde se aplican estos valores. 

## 2.6 Literal `None`.

Un literal especial que es parte de Python se expresa como `None`. Es un objeto de tipo `NoneType` y es utilizado para representar la **ausencia de un valor**.

