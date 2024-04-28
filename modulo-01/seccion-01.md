# 1. Introducción a la programación.

## 1.1 Funcionamiento de un programa de computadora.

Un computador no es funcionable sin un **programa**.

Si bien los computadores son capaces de realizar tareas complejas, no "nacen" con dicha habilidad. Es decir, no es algo innato en estos.

En general, los computadores:

- Ejecutan tareas muy sencillas.
- Solo evaluan operaciones fundamentales, tales como la suma y la división.

La particularidad es que ambos trabajos los hace **rápido** y, virtualmente, puede **repetirlos** las veces que uno quiera.

Para que un computador pueda realizar tanto tareas sencillas como más complejas, necesita que un usuario le indique previamente un **conjunto de instrucciones** para que las haga, conocido como **programa computacional** o **programa**.

Para que un computador pueda ejecutar las instrucciones que un usuario quiere que realice, debe escribirlas en un **lenguaje** que permita al primero traducirlas a su "idioma" de máquina.


## 1.2 Lenguajes naturales y lenguajes de programación.

En términos generales, un **lenguaje** es un **medio** (y una herramienta) para **expresar y registrar ideas**.

Tipos de lenguajes (o lenguas):

1. Corporal.
2. Materna.
3. De máquina.

Los dos primeros lenguajes señalados arriba pueden englobarse como **lenguajes naturales**. Son los que utilizamos las personas habitualmente y se caracterizan por:

- Tener un nivel de complejidad que puede ser interpretado por nosotros mismos.
- Estar evolucionando constante y naturalmente: Surgen nuevas palabras, mientras que otras van desapareciendo.

El tercer tipo de lenguaje mencionado anteriormente, conocido como **lenguaje de máquina**, es el utilizado por los computadores para ejecutar un programa.

El lenguaje de máquina se caracteriza por ser **muy rudimentario**. Consiste de un **conjunto predeterminado de comandos** sencillos de reconocer, también llamado **Lista de instrucciones** (o IL de *instruction list*).

Un computador puede ser diferenciado en su tipo mediante:

- El tamaño de su IL.
- Las instrucciones en sí, que pueden ser distintas para diferentes modelos.

Similitud entre las personas y los computadores: Ambos grupos pueden manejar distintos lenguajes a la vez, pero se diferencian en que las primeras lo hacen de manera natural.


## 1.3 Elementos que conforman a un lenguaje.

Todo lenguaje se compone de **cuatro** elementos:

1. **Alfabeto**: Conjunto de **símbolos** para **armar palabras** en un idioma determinado.
2. **Léxico**: Conjunto de **palabras** que ofrece un lenguaje a un usuario. También se conoce como diccionario.
3. **Sintáxis**: Conjunto de **reglas** usadas para **determinar** si una cadena de palabras forman una **oración válida**.
4. **Semántica**: Conjunto de **reglas** que determinan **si una frase hace sentido**.


## 1.4 Lenguajes de máquina y lenguajes de alto nivel.

El **lenguaje de máquina** es el alfabeto de un computador. Podríamos usarlo para escribir los comandos que queremos que ejecute, pero **es muy ilegible** para nosotros. Por esta razón, utilizamos un lenguaje intermediario para escribir las ILs que, posteriormente, son traducidas a idioma de máquina, llamado **Lenguaje de programación de alto nivel**.

Los lenguajes de programación de alto nivel (o, simplemente, lenguajes de programación) son más entendibles porque usan **símbolos, palabras y convenciones** legibles para nosotros, facilitando así la tarea de expresar comandos al computador.

De los lenguajes de programación surgen dos conceptos adicionales:

1. **Código fuente** (*source code*): Programa escrito en un lenguaje de programación de alto nivel.
2. **Archivo fuente** (*source file*): Archivo que aloja al código fuente.

Por otra parte, cuando el código fuente es traducido a lenguaje de máquina, este pasa a ser llamado como **código de máquina** (*machine code*).


## 1.5 Compilación e interpretación.

La **programación informática** puede ser definida como:

> El acto de componer los elementos elegidos de un lenguaje de programación para que genere el efecto deseado.

El programa que resulta de dicho acto, debe ser correcto:

- **Alfabéticamente**: Debe estar escrito en un alfabeto reconocible.
- **Léxicamente**: Es necesario dominar el "diccionario" de un lenguaje de programación.
- **Sintácticamente**: Se debe obedecer las reglas del lenguaje que se está usando para programar.
- **Semánticamente**: El programa tiene que hacer sentido.

De cumplirse lo señalado en los cuatro puntos de arriba, al ejecutar el programa el computador realizará la tarea que esperamos que realice.

Un programa escrito en lenguaje de programación debe ser traducido a lenguaje de máquina para que sea ejecutado. Este proceso puede realizarse mediante uno de estos dos programas computacionales:

1. **Compilador**: Convierte el archivo fuente a uno ejecutable (`.exe`) que aloja al código de máquina. Si uno modifica el primero, debe volver a crear el segundo (no se modifica por sí solo).
2. **Interpretador**: Simplemente traduce el código fuente a código de máquina cada vez que es ejecutado.

Por lo tanto, el interpretador no genera un archivo nuevo del que contiene el código fuente, a diferencia del compilador.


## 1.6 El interpretador.

Los interpretadores leen el código fuente al igual como lo hacemos en la cultura occidental: De arriba hasta abajo y de izquierda a derecha.

Mientras hacen la lectura del código fuente, los interpretadores van revisando si las líneas de este último son correctas o si tienen errores alfabéticos, léxicos, sintácticos o semánticos. Al encontrar uno de ellos, terminará la ejecución del programa y enviará un mensaje de error.

En cuanto a los mensajes de error, el interpretador en ocasiones indicará cuál fue y dónde está ubicado en el código fuente. Sin embargo, no siempre nos dará una explicación explícita, porque el computador como un todo nunca sabrá nuestra intención detrás del programa.

## 1.7 Modelos de compilado e interpretación: Ventajas y desventajas.

Las principales ventajas y desventajas del compilador son las siguientes:

|                                Ventajas                                |                                    Desventajas                               |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------------|
|La ejecución del código traducido es más rápido.                        |El proceso de compilación puede durar mucho tiempo.                           |
|El usuario final no necesita tener el compilador para usar el código.   |Es necesario tener tantos compiladores como plataformas de hardware para que pueda ejecutarse el código.|
|El código traducido es almacenado usando en lenguaje de máquina.        |                                                                               | 

En cuanto al interpretador, sus ventajas y desventajas son:

|                       Ventajas                                  |                                         Desventajas                                         |
|:----------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
|El programa puede ser ejecutado apenas uno termina de escribirlo.| El código usará capacidad del computador para ejecutarse, por lo que no siempre aquello será rápido|
|El código solo es almacenado en lenguaje de programación, facilitando su portabilidad.| Tanto uno como el usuario final debemos usar el mismo interpretador para ejecutar el código.|


