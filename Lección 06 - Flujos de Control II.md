# Bucles

Un objeto **iterable** es un objeto que puede devolver uno de sus elementos a la vez. Estos objetos pueden incluir tipos de secuencia, como cadenas, listas y tuplas, así como tipos que no son de secuencia, como diccionarios y archivos.

## Bucles For

Veamos un ejemplo para conocer como implementar un bucle `for`:

```py
ciudades = ['CDMX', 'Monterrey', 'Guadalajara', 'Aguascalientes']
for ciudad in ciudades:
    print(ciudad)
print("¡Listo!")
```
**Componentes de un bucle `for`**  :

1. La primera línea del bucle comienza con la palabra clave `for`, que indica que se trata de un bucle `for`.

2. A continuación se indica `ciudad in ciudades`, lo que indica que la `ciudad` es la variable de iteración, y `ciudades` es el iterable sobre el que está trabajando el bucle. En la primera iteración del bucle, `ciudad` obtiene el valor del primer elemento en `ciudades`, que es `"CDMX"`.

3. La línea de encabezado del bucle `for` siempre termina con dos puntos `:` .
Después del encabezado del bucle `for` hay un bloque de código indentado, el cuerpo del bucle, que se ejecutará en cada iteración de este bucle. Solo hay una línea en el cuerpo de este bucle: `print (ciudad)`.

4. Después de que el cuerpo del bucle se haya ejecutado, todavía no pasamos a la siguiente línea; volvemos a la línea de encabezado `for`, donde la variable de iteración toma el valor del siguiente elemento del iterable. En la segunda iteración del ciclo anterior, la ciudad toma el valor del siguiente elemento en las ciudades, que es `"Monterrey"`.

5. Este proceso se repite hasta que el bucle haya iterado a través de todos los elementos del iterable. Luego, pasamos a la línea que sigue al cuerpo del bucle; en este caso, imprime `"¡Listo!"`. Podemos decir cuál es la siguiente línea después del cuerpo del bucle porque no tiene indentación. ¡Aquí hay otra razón por la que prestar atención a la indentación es muy importante en Python!

### Usando la función `range()` con bucles `for`

`range ()` es una función incorporada, utilizada para crear una secuencia iterativa de números. Con frecuencia usará `range ()` con un bucle `for` para repetir una acción un cierto número de veces. Como en este ejemplo:

```py
for i in range(3):
    print("¡Hola!")
```

Salida:

```
¡Hola!
¡Hola!
¡Hola!
```

#### range(start=0, stop, step=1)

La función `range()` toma **tres argumentos enteros**, el primero y el tercero son opcionales:  

- `start`. Es el primer número de la secuencia. Si no se especifica, `start` por defecto es 0.  

- `stop`. Es 1 más que el último número de la secuencia. Este argumento debe ser especificado.  

- `step`. Es la diferencia entre cada número en la secuencia. Si no se especifica, el `step` predeterminado es 1.

### Creando y modificando listas

```py
ciudades = ['cdmx', 'monterrey', 'guadalajara', 'aguascalientes']
ciudades_mayusculas = []

for ciudad in ciudades:
    ciudades_mayusculas.append(ciudad.title())
```

```py
ciudades = ['cdmx', 'monterrey', 'guadalajara', 'aguascalientes']

for indice in range(len(ciudades)):
    ciudades[indice] = ciudades[indice].title()
```

### [Lección 06 - Ejercicio 03](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2006-03.ipynb)

### Construyendo Diccionarios

#### Usando un bucle `for`

```py
titulo_libro =  ['don', 'quijote', 'de', 'la', 'mancha', 'cien', 'años', 'de', 'soledad','crimen','y','castigo','el','conde','de','montecristo','el','principito']
```
```py
contador_palabras = {}
```
```py
for palabra in titulo_libro:
    if palabra not in contador_palabras:
        contador_palabras[palabra] = 1
    else:
        contador_palabras[palabra] += 1
```

#### Usando el método `get()`

```py
titulo_libro =  ['don', 'quijote', 'de', 'la', 'mancha', 'cien', 'años', 'de', 'soledad','crimen','y','castigo','el','conde','de','montecristo','el','principito']
```
```py
contador_palabras = {}
```
```py
for palabra in titulo_libro:
    contador_palabras[palabra] = contador_palabra.get(palabra, 0) + 1
```

### Iterando a través de Diccionarios

```py
elenco = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
```
```py
for llave in elenco:
    print(llave)
```
Otra forma:

```py
for llave, valor in elenco.items():
    print("Actor: {}    Personaje: {}".format(llave, valor))
```

### [Lección 06 - Ejercicio 04](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2006-04.ipynb)

## Bucles While

Los bucles `for` son un ejemplo de "**iteración definida**", lo que significa que el cuerpo del bucle se ejecuta un número predeterminado de veces. Esto difiere de una "**iteración indefinida**", que es cuando un ciclo se repite un número desconocido de veces y termina cuando se cumple alguna condición, que es lo que sucede en un bucle `while`.

Veamos un ejemplo:

```py
baraja = [4, 11, 8, 5, 13, 2, 8, 10]
mano = []

# agrega a mano los elementos de la lista baraja mientras la suma total sea menor a 17
while sum(mano) < 17:
    mano.append(baraja.pop())
```

**Componentes de un bucle `while`**  :

1. La primera línea del bucle comienza con la palabra clave `while`.

2. A continuación se indica la condición que debe cumplirse para que se ejecute el bloque dentro del `while`.

3. La línea de encabezado del bucle for siempre termina con dos puntos `:`.

4. Después del encabezado del bucle `while` hay un bloque de código indentado, el cuerpo del bucle, que se ejecutará en cada iteración de este bucle. Solo hay una línea en el cuerpo de este bucle: `mano.append(baraja.pop())`.

### [Lección 06 - Ejercicio 05](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2006-05.ipynb)

## Break & Continue

A veces necesitamos más control sobre cuándo debe terminar un bucle, o saltar una iteración. En estos casos, usamos las palabras clave `break` y `continue`, que se pueden usar tanto en bucles `for` como `while`.  

- `break` termina un bucle  

- `continue` omite una iteración de un bucle  

Un ejemplo sería concatenar los elementos de una lista en una sola cadena, pero solo hasta que el tamaño de la cadena no exceda los 140 caracteres:

```py
titulares = ["Oso Comido por un Hombre",
             "Legisladores Anuncian Nuevas Leyes",
             "Ciudadano Descubre Violencia Inherente en el Sistema",
             "Gato Rescata a Bombero Atorado en Arbol",
             "Valiente Caballero Huye del Dragón",
             "Libro del Mes: Totalmente Horrible"]

teletipo_noticias = ""
for titular in titulares:
    teletipo_noticias += titular + " "
    if len(teletipo_noticias) >= 140:
        teletipo_noticias = teletipo_noticias[:140]
        break

print(teletipo_noticias)
```

### [Lección 06 - Ejercicio 06](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2006-06.ipynb)


# Zip & Numerate

`zip` y `enumerate` son funciones incorporadas útiles cuando trabajamos con bucles.

### Zip

`zip` devuelve un iterador que combina múltiples iterables en una secuencia de tuplas. Cada tupla contiene los elementos en esa posición de todos los iterables. Por ejemplo:

```py
list(zip(['a', 'b', 'c'], [1, 2, 3]))
```
Resultado:

```py
[('a', 1), ('b', 2), ('c', 3)]
```

Si necesitamos hacer un Unzip:

```py
una_lista = [('a', 1), ('b', 2), ('c', 3)]
letras, numeros = zip(*una_lista)
```

Otro ejemplo:

```py
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
etiquetas = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

puntos = []
for punto in zip(etiquetas, x_coord, y_coord, z_coord):
    puntos.append("{}: {}, {}, {}".format(*punto))

for punto in puntos:
    print(punto)
```    

### Enumerate

`enumerate` es una función que devuelve un iterador de tuplas que contienen índices y valores de una lista. A menudo es útil cuando se desea el índice junto con cada elemento de un iterable en un bucle.

```py
letras = ['a', 'b', 'c', 'd', 'e']
for i, letra in enumerate(letras):
    print(i, letra)
```

Resultado:

```py
0 a
1 b
2 c
3 d
4 e
```

# List Comprehensions

En Python, puede crear listas de manera muy rápida y concisa con List Comprehensions.

En un ejemplo normal:

```py
ciudades = ['cdmx', 'monterrey', 'guadalajara', 'aguascalientes']
ciudades_mayusculas = []
for ciudad in ciudades:
    ciudades_mayusculas.append(ciudad.title())
```

Usando List Comprehensions:

```py
ciudades = ['cdmx', 'monterrey', 'guadalajara', 'aguascalientes']
ciudades_mayusculas = [ciudad.title() for ciudad in ciudades]
```

Otro ejemplo:

```py
cuadrados = [x**2 for x in range(9) if x % 2 == 0]
```

Un ejemplo más:

```py
cuadrados = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```

### [Lección 06 - Ejercicio 07](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2006-07.ipynb)
