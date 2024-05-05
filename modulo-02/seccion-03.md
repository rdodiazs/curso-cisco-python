# 3. Operadores y herramientas de manipulación de datos.

## 3.1 Operadores básicos.

En Python es posible realizar **siete** operaciones aritméticas básicas. A continuación se muestran junto con los símbolos de sus operadores:

1. Suma: `+`
2. Resta: `-`
3. Multiplicación: `*`
4. División flotante: `/`
5. División entera: `//`
6. Módulo: `%`
7. Exponenciación: `**`

Revisemos las últimas cuatro operaciones señaladas arriba.

La **división flotante**, `/`, es aquella división cuyo resultado corresponde a un **número flotante**. De este modo, se puede deducir correctamente que la **división entera** (`//`) es la operación en la que se obtiene un **número entero**.

En cuanto a la operación **módulo**, expresada como `%`, es aquella que entrega el **resto de una división**. Por ejemplo,

```
>> 2 % 2
0
```

porque `2//2 == 1` y su resto es `0`. Este último valor es el que entrega la operación módulo.

Finalmente, la **operación exponenciación** `**` entrega el valor de una **potencia**. Por ejemplo, `2**2 == 4` porque se refiere a $2^{2} = 4$.

## 3.2 Operadores unarios y binarios.

Los operadores básicos vistos en la sección 3.1 también se conocen como **operadores binarios**, puesto que se ejecutan si **hay valores numéricos tanto a sus izquierdas como derechas**.

No obstante, los operadores `+` y `-` también puede ejecutarse como **operadores unarios**, porque también pueden ejecutarse **solo con un valor numérico a sus izquierdas**. En este caso, funcionan como los **signos de dichos números**.


## 3.3 Operadores y sus prioridades.

A continuación se muestran el orden de prioridad que tiene cada operador básico en Python:

|Prioridad |            Nombre           |       Símbolo       |   Tipo   |
|:--------:|:---------------------------:|:-------------------:|:--------:|
|     1    |         Exponenciación      |         `**`        | Binario  |
|     2    |      Positivo y negativo    |       `+` y `-`     | Unarios  |
|     3    |  Mult, divisiones y módulo  | `*`, `/`, `//` y `%`| Binarios |
|     4    |          Suma y resta       |       `+` y `-`     | Binarios |