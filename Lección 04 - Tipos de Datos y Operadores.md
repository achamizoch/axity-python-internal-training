# Tipos de Datos y Operadores

En esta lección conoceremos aprenderemos acerca de:

- Operadores
	- Aritméticos
	- De Asignación
	- De Comparación
	- Lógicos

- Tipos de Datos: Integers, Floats, Booleans, Strings

- Conversión de tipos de datos

- Funciones incorporadas (Built-in)

- Guías de estilo (Best Practices)

## Operadores

### Aritméticos

-   `+` Suma
-   `-` Resta
-   `*` Multiplicación
-   `/` División
-   `%` Residuo (el remanente después de una división)
-   `**` Exponenciación
-   `//` Divide y redondea al entero más cercano

### Operadores de Asignación

![img_04_dt_01](images/img_04_dt_01.png)

> Use JupyterLab para probar los siguientes operadores

Para asignar un valor a una variable:

```py
x = 3
y = 4
z = 5
```

Lo anterior es igual a:

```py
x, y, z = 3, 4, 5
```

## Booleanos, Operadores de Comparación y Operadores Lógicos

### Operadores de Comparación

| Símbolo/Caso de Uso | Booleano | Operación |
|--|--|--|
| 5 < 3	| False	| Menor que 		|
| 5 > 3	| True	| Mayor que	|
| 3 <= 3| True	| Menor o igual a	|
| 3 >= 5| False	| Mayor o igual a	|
| 3 == 5| False	| Igual a 		|
| 3 != 5| True 	| No igual a 		|

### Operadores Lógicos

| Símbolo/Caso de Uso | Booleano | Operación |
|--|--|--|
| 5 < 3 `and` 5 == 5	| False	| `and` evalúa si todas las declaraciones son ciertas (True)|
| 5 < 3 `or` 5 == 5	| True	| `or` evalúa si alguna de las declaraciones es cierta (True)|
| `not` 5 < 3		| True	| `not` Invierte el valor del resultado|

###

## Tipos de Datos

### Enteros y Flotantes (Integer, Float)

-   **int** - para valores enteros
-   **float** - para valores decimales o de punto flotante

```py
x = int(4.7)   # x es ahora un entero = 4
y = float(4)   # y es ahora un valor de punto flotante = 4.0

```

Para checar el tipo de datos de un objeto podemos usar la función `type`:

```py
>>> print(type(4))
int
>>> print(type(3.7))
float
>>> print(type('esto'))
str
>>> print(type(True))
bool
```

### Cadena (String)

Las cadenas en Python se muestran como el tipo variable `str`. Se puede definir una cadena con comillas dobles `"` o comillas simples `'`

> Si la cadena que está creando contiene uno de estos dos caracteres, se debe tener cuidado para asegurarse que el código no genere un error.

```py
>>> mi_cadena = '¡esta es una cadena!'
>>> mi_cadena2 = "¡esta también es una cadena!"
```

Podemos incluir el caracter `\` en una cadena para incluir comillas simples como parte de la misma cadena:

```py
>>> esta_cadena = 'El título del libro es \'Don Quijote\'.'
>>> print(esta_cadena)
```

```py
El título del libro es 'Don Quijote'.
```

**¿Qué pasa si en el ejemplo anterior no incluimos el caracter `\`?**

Para acceder una cadena:

```py
>>> primera_palabra = 'Hola'
>>> segunda_palabra = 'Mundo'
>>> print(primera_palabra + segunda_palabra) # Concatenar dos cadenas
HolaMundo

>>> print(primera_palabra + ' ' + segunda_palabra)
Hola Mundo

>>> print(primera_palabra * 5)
HolaHolaHolaHolaHola

>>> print(len(primera_palabra))
4
```

```py
>>> primera_palabra[0]
H
>>> primera_palabra[1]
o
```

Para obtener la longitud de una cadena podemos usar la función `len()`, la cual es una función incorporada (Built-in) de Python:

```py
print(len("ababa") / len("ab"))
2.5
```

### Booleanos

Para definir un tipo de dato booleano:

```py
x = True
y = False

print(type(x))
type(y)
```

## Conversión de datos

Para poder convertir un tipo de datos a otro, podemos usar las siguientes funciones de conversión (cast):

```py
>>> print(str(14))
'14'

>>> print(int(4.7))
4

>>> print(float(5))
5.0

>>> print(bool(1))
True
```

## Funciones incorporadas (Built-in)

Algunos métodos de cadena que podemos usar:

![img_04_dt_02](images/img_04_dt_02.png)

Para conocer todos los métodos que podemos usar, véase la [documentación de Python](https://docs.python.org/3.7/library/stdtypes.html#string-methods).

### Un método importante

El método cadena `format()` es uno de los métodos más útiles y que estaremos usando en el transcurso de nuestro curso. Este método reemplaza o complementa partes de una cadena con los valores de otros objetos o variables. Algunos ejemplos de cómo podemos usar este método:

```py
print("Juan tiene {} globos".format(27))
```

```py
animal = "perro"
accion = "muerde"
print("¿Tu {} {}?".format(animal, accion))
```

```py
cadena_maria = "A María le gustan {} y {}"
print(cadena_maria.format("las matemáticas", "la estadística"))
```

### Otro método interesante

Otro método de cadena que puede ser muy útil es el método `split()`. Este método divide una cadena en palabras y lo devuelve como una lista. Veamos algunos ejemplos y usos:

```py
nueva_cadena = "La vaca saltó sobre la luna."
nueva_cadena.split()
```
```py
['La', 'vaca', 'saltó', 'sobre', 'la', 'luna.']
```


Especificando un separador:

```py
nueva_cadena.split(' ', 3)
```
```py
['La', 'vaca', 'saltó', 'sobre la luna.']
```

Limitando el número de elementos de la lista

```py
nueva_cadena.split(None, 3)
```
```py
['La', 'vaca', 'saltó', 'sobre la luna.']
```
