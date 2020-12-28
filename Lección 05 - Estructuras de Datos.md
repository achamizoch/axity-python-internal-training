# Estructuras de Datos

En esta lección conoceremos los diferentes tipos de estructuras de datos usados en Python:

- Tipos de estructuras de datos:
	- Listas
	- Tuplas
	- Conjuntos
	- Diccionarios
	- Estructuras de datos compuestas

- Operadores  de Identidad

## Listas

Las **estructuras de datos** son contenedores que organizan y agrupan los tipos de datos de diferentes formas. Una **lista** es una de las estructuras de datos más comunes y básicas en Python.  

Las listas deben ser creadas usando **corchetes** y pueden contener cualquier combinación de los tipos de datos (numérico y alfanumérico).

Para ejecutar los siguientes comandos use JupyterLab.

### Crear una lista

```py
lista_de_elementos = [1, 3.4, 'una cadena', True]
```

### Acceder a un elemento de la lista

```py
>>> lista_de_elementos[0]
1
```

```py
>>> lista_de_elementos[len(lista_de_elementos)]

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-34-f88b03e5c60e> in <module>()
----> 1 lst[len(lst)]

IndexError: list index out of range

```

> Note que para acceder al último elemento de la lista, se debe especificar el valor del tamaño de la lista menos 1 (len() - 1). Pruebe el siguiente comando para confirmar esto.

```py
>>> lista_de_elementos[len(lista_de_elementos) - 1]
True
```

### Rebanar y cortar (Slice & Dice)
```py
>>> lista_de_elementos = [1, 3.4, 'una cadena', True]
>>> lista_de_elementos[1:1]
[]
```
```py
>>> lista_de_elementos = [1, 3.4, 'una cadena', True]
>>> lista_de_elementos[1:2]
[3.4]
```
```py
>>> lista_de_elementos = [1, 3.4, 'una cadena', True]
>>> lista_de_elementos[1:3]
[3.4, 'una cadena']
```
```py
>>> lista_de_elementos = [1, 3.4, 'una cadena', True]
>>> lista_de_elementos[1:4]
[3.4, 'una cadena', True]
```
```py
>>> lista_de_elementos = [1, 3.4, 'una cadena', True]
>>> lista_de_elementos[1:5]
[3.4, 'una cadena', True]
```

### IN o NOT IN

```py
>>> 'esta' in 'esta es una cadena'
True
>>> 'en' in 'esta es una cadena'
True
>>> 'esuna' in 'esta es una cadena'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False
```


## Mutabilidad y Orden

El concepto de **mutabilidad** en Python indica si podemos o no cambiar un objeto, una vez que se ha creado. Si un objeto (como una lista o cadena) se puede cambiar (como una lista), se considera **mutable**.

Sin embargo, si un objeto no se puede cambiar, entonces el objeto se considera **inmutable**.

Ejemplo de mutabilidad:

```py
>>> mi_lista = [1, 2, 3, 4, 5]
>>> mi_lista[0] = 'uno'
>>> print(mi_lista)
['uno', 2, 3, 4, 5]
```

Ejemplo de un objeto inmutable:
```py
>>> mi_cadena = "Hola Mundo"
>>> mi_cadena[0] = 'M'
```

El concepto de **orden** en Python indica si la posición de un elemento en el objeto se puede utilizar para accederlo. Ambas cadenas y listas están ordenadas. Podemos usar el orden para acceder a partes de una lista y cadena.

En lecciones posteriores veremos que, para los diferentes tipos de datos, es importante tener en cuenta sus propiedades de mutabilidad y ordenamiento, para poder acceder a ellos y manipularlos.

## Funciones básicas

1. `len()` devuelve el número de elementos que hay en una lista.

2. `max()` devuelve el elemento más grande de la lista. La forma en que se determina el elemento más grande depende del tipo de objetos que estén en la lista.
	- El elemento máximo en una lista de números es el número más grande.
	- El elemento máximo en una lista de cadenas es el último elemento ordenado alfabéticamente.
	- La función `max()` no está definida para listas que contienen elementos de diferentes tipos que no son compatibles.

3. `min()` devuelve el elemento más pequeño de una lista. `min()` es lo opuesto a `max()`, que devuelve el elemento más grande de una lista.

4. `sorted()` devuelve una copia de una lista ordenada de menor a mayor, dejando la lista sin cambios.

Probemos:

```py
mi_lista_de_cadenas = ['Z', 'ALZ', 'B']
max(mi_lista_de_cadenas)
sorted(mi_lista_de_cadenas)
```

4. `join()`. Es un método de cadena que toma una lista de cadenas como argumento y devuelve una cadena que consta de los elementos unidos por un separador.

```py
mi_separador= "\n"
mi_lista_de_cadenas = ["Este", "es", "mi", "curso", "Python"]
nueva_cadena = mi_separador.join(mi_lista_de_cadenas)

print(nueva_cadena)
```

5. `append()`. Este método agrega un elemento al final de una lista.

```py
letras = ['a', 'b', 'c', 'd']
letras.append('z')

print(letras)
```

6. `pop()`. Este método elimina un elemento de una lista. Si no se especifica un valor, se elimina el último elemento (en otros tipos de estructuras, si no se define un valor puede eliminar el primer elemento)

```py
letras = ['a', 'b', 'c', 'd']
letras.pop(0)

print(letras)
```

7.  `split()`. Divide una cadena y como resultado devuelve una lista.

```py
verso = "si puedes mantener la cabeza en su sitio cuando todos a tu alrededor la pierden y te culpan a ti   si puedes seguir creyendo en ti mismo cuando todos dudan de ti     pero también aceptas que tengan dudas   si puedes esperar y no cansarte de la espera      o si siendo engañado no respondes con engaños   o si siendo odiado no incurres en el odio      Y aun así no te las das de bueno ni de sabio"
print(verso, "\n")

verso_lista = verso.split()
print(verso_lista, '\n')
```

## Tuplas

Una **tupla** es otro tipo de estructura útil. Es un tipo de datos para secuencias **inmutables, ordenadas** de elementos. A menudo se usan para almacenar información relacionada. Considere este ejemplo que involucra latitud y longitud:

```py
ubicacion = (13.4125, 103.866667)

print("Latitud:", ubicacion[0])
print("Longitud:", ubicacion[1])
```

Probemos lo siguiente:

```py
ubicacion[0] = 12.1
```
¿'Una Tupla es un objeto **mutable**?

¿'Una Tupla es un objeto **ordenado**?

## Conjunto

Un **conjunto** es un tipo de datos para colecciones **mutables, no ordenadas** de elementos **únicos**. Una aplicación de un conjunto es eliminar rápidamente los duplicados de una lista.

```py
numeros = [1, 2, 6, 3, 1, 1, 6]
numeros_unicos = set(numeros)

print(numeros_unicos)
```

### [Lección 05 - Ejercicio  01](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2005-01.ipynb)

## Diccionarios

Un **diccionario** es un tipo de dato **mutable** que almacena asignaciones de claves únicas a valores:

```py
elementos = {"hidrogeno": 1, "helio": 2, "carbono": 6}

print(elementos["helio"])

elementos["litio"] = 3  # Insertar "litio" con el valor 3 dentro del diccionario
```

```py
print("carbono" in elementos)

print(elementos.get("litio"))
print(elementos.get("hidrogeno"))

print(elementos["hidrogeno"])
```

¿Qué diferencia hay entre usar get() o corchetes ([])?

```py
print(elementos["litio"])
```

## Operadores de identidad

Operadores:
- `is` evalúa si ambos objetos contienen el mismo valor

- `is not` evalúa si ambos objetos no contienen el mismo valor

Probemos:

```py
n = elementos.get("litio")
print(n is None)
print(n is not None)
```

# Estructuras de datos compuestas

Una característica interesante en Python es el poder incluir contenedores dentro de otros contenedores, para crear estructuras de datos compuestos. Por ejemplo:

```py
elementos = {"hidrogeno": {"numero": 1,
                         "peso": 1.00794,
                         "simbolo": "H"},
                 "helio": {"numero": 2,
                         "peso": 4.002602,
                         "simbolo": "He"}}
```

Para acceder a este diccionario anidado:

```py
helio = elementos["helio"]
hidrogeno_peso = elementos["hidrogeno"]["peso"]
```

Para agregar una nueva llave al diccionario:

```py
oxigeno = {"numero":8,"peso":15.999,"simbolo":"O"}  # crear un diccionario
elementos["oxigeno"] = oxigeno  # asignar el diccionario al diccionario compuesto
print('elementos = ', elementos)
```

| Estructura de Datos | Ordenado | Mutable | Constructor | Ejemplo |
|--|--|--|--|--|
| Lista 	| Si | Si | `[ ]` o `list()`	| `[5.7, 4, 'si', 5.7]` |
| Tupla 	| Si | No | `( )` o `tuple()`	| `(5.7, 4, 'si', 5.7)` |
| Conjunto	| No | Si | `{}`* o `set()`	| `{5.7, 4, 'si'}`	 |
| Diccionario 	| No | No | `{ }` o `dict()`	| `{'Jun': 75, 'Jul': 89}` |

* Puede usar `{}` para definir un set como este `{1, 2, 3}`. Sin embargo, si dejan las llaves vacías, Python creará un diccionario vacío. Por lo que, para crear un **set vacío**, se debe usar `set()`.

** Un diccionario por sí mismo es mutable, pero cada una de las llaves individuales debe ser inmutable.

### [Lección 05 - Ejercicio  02](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2005-02.ipynb)


### [Lección 05 - Ejercicio  03](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2005-03.ipynb)
