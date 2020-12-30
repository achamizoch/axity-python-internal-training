# Introducción a NumPy & Pandas


Tanto **NumPy** como los **Pandas** a menudo se usan juntos, ya que la librería de Pandas depende en gran medida de la matriz **NumPy** para la implementación de objetos de datos de **Pandas** y muchas de sus características compartidas. Además, **Pandas** se basa en la funcionalidad proporcionada por **NumPy**. Ambas bibliotecas pertenecen a lo que se conoce como [SciPy](https://www.scipy.org/), un conjunto de librerías de Python utilizadas para la ciencia de datos.

> La distribución Anaconda Scientific Python instala Pandas y NumPy como parte de la instalación predeterminada.

## NumPy (Numerical Python)

NumPy permite trabajar con arreglos y matrices de datos de alto desempeño. Su principal objeto o estructura de datos es el **ndarray**, un tipo de arreglo N-dimensional el cual describe una colección de **elementos** del mismo tipo.

Por ejemplo:

```py
import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
a1
```

Resultado:

```py
array([1, 2, 3, 4, 5])
```
En los siguientes ejercicios explicaremos de forma general el uso e implementación de estructuras de **NumPy**:

### [Lección 10 - Ejercicio 01](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2010-01.ipynb)


## Pandas (Panel Data)

Pandas incorpora dos estructuras de datos adicionales en Python:

- **Pandas Series**. Una serie es el primer bloque de construcción principal de **Pandas**. Una serie representa una matriz indexada etiquetada unidimensional, basada en una matriz de datos **NumPy**.

- **Pandas DataFrame**. Son estructuras de datos bidimensionales con filas y columnas etiquetadas, que pueden contener muchos tipos de datos. Similar a Excel, podemos pensar en **Pandas DataFrames** como algo similar a una hoja de cálculo. Podemos crear **Pandas DataFrames** manualmente o cargando datos desde un archivo.

En los siguientes ejercicios explicaremos de forma general el uso e implementación de estructuras de **Pandas**:

### [Lección 10 - Ejercicio 02](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2010-02.ipynb)

### [Lección 10 - Ejercicio 03](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2010-03.ipynb)

### [Lección 10 - Ejercicio 04](http://localhost:8888/lab/tree/my_python_repo/Ejercicio%2010-04.ipynb)

## Diferencias clave  

- Ambas bibliotecas son particularmente utilizadas en la Ciencia de Datos, ML e IA.

- Ambos se utilizan para almacenar n número de valores o datos.  

- **Pandas** proveé algunos objetos poderosos como **DataFrames** y **Series** que son muy útiles para trabajar y analizar datos, mientras que **NumPy** proporciona objetos para matrices multidimensionales,

- **Pandas** proporciona un objeto de tipo tabla (2D) llamado **DataFrame** que trabaja en memoria.

- **Pandas** funciona cuando los datos están en formato tabular, mientras que **NumPy** funciona muy bien cuando los datos son numéricos.

- **NumPy** consume menos memoria en comparación con los **Pandas**.  

- **NumPy** funciona muy bien cuando hay 50k filas o menos, mientras que los **Pandas** funciona realmente bien cuando hay alrededor de 500k filas o más.
