# Estructura del Proyecto

Este proyecto presenta una simulación en donde se tiene una cierta cantidad N de partículas o planetas, los cuales se comportarán siguiendo la ley de gravitación universal. Además, cada una de las partículas tendrá una forma aleatoria, la cual será elegida a partir de una lista donde se tendrán diferentes opciones predeterminadas. 

Añadido a lo anterior, la simulación también permitirá que las partículas se fusionen en el caso de que estas se acerquen más allá de cierto radio, el cual puede ser elegido por el usuario. La estructura del proyecto es la siguiente: 

1. .venv
2. processing
    2.1 __init__.py
    2.2 distribuciones.py
    2.3 objeto.py
    2.4 simulacion.py
3. tests
    3.1 tests.py
4. config.py
5. main.py
6. makefile
7. requirements.txt

A continuación, vamos a describir que función tiene cada uno de los archivos presentados anteriormente y desglosaremos el funcionamiento del código o el contenido de cada uno de estos archivos.

## 1. .venv

Esta carpeta contiene todo lo necesario para la creación de un entorno virtual, es decir, una instalación aislada de python con sus propios paquetes. Este aislamiento de dependencias es muy útil, pues nos deja instalar librerias sin que estas interfieran de manera global con otros proyectos. 

Esto quiere decir, que si por ejemplo, un proyecto necesita la versión 1.21 de numpy y otro necesita la versión 1.26, podemos usar un ambiente virtual en ambas para que los dos funcionen sin conflicto. 

## 2. Processing

Dentro de esta carpeta, están todos los código que sirven para la creación de objetos y la simulación. Estos están divididos en diferentes archivos con el objetivo de que el proyecto sea escalable y que sea más fácil editar cierta parte del código si fuera necesario. A continuaci+on describimos lo que hace cada uno de los archivos y las funciones dentro de estos.

## 2.1 __init__.py

Este es unu archivo vacío pero se usa para indicar que un directorio es un paquete de Python. Su función principal es permitir que Python trate esa carpeta como un módulo que puede ser importado.

## 2.2 Distribuciones

En este código, definimos una sola clase llamada **Generador**, con diferentes métodos para generar valores aleatorios. Para ello utilizamos la libreria random y también llamamos a un archivo externo de nombre **config**, en el cual el usuario puede ingresar ciertos parámetros definidos para la generación de los números.

### Generar_masa_aleatoria()
Este método genera valores aleatorios a partir de una distribución Gaussiana. En este caso, se usa config.DATO para llamar a algún parámetro que se encuentre dentro del archivo config y usarlo como parámetro dentro de la función que nos da la distribución.

### Generar_posicion_uniforme()
Este método nos genera una posición (x, y) dentro de un área definida por los parámetros ancho y alto. Estos números son generados a partir de una distribución uniforme. La parte de margen=100 evita que los objetos aparezcan demasiado cerca del borde. 

## 2.3 Objeto

En este código se usan las librerias pygame, random, math y de nuevo se importa el módulo config para poder obtener diferentes parámetros.

Dentro de la clase **Particula** tenemos diferentes métodos, que son los siguiente: 

### Constructor __init__()
Este nos ayuda a definir una partícula con cierta posición inicial (x, y), una masa, una velocidad (vx, vy) y también el color de la particula, el cual será elegido de manera aleatoria en caso de que no se especifique el color deseado. De igual manera, la forma de la partícula será elegida de manera aleatoria si no se especifica la figura deseada. Para la forma de la partícula hay una lista con tres diferentes opciones de las cuales se pueden elegri. Más adelante se definirá como se crea cada una de estas figuras. 

### actualizar_pos()
Este método permite que la posición se actualice, dependiendo de la velocidad que tenga una partícula. Esto se hace de la forma self.x += self.vx. Además, ajusta la posición para que esta no se pase del límite de la pantalla. 

También podemos ver (dentro de los if) que pasará en caso de que alguna partícula toque el borde de la pantalla. Lo que se hace en este caso, es invertir la velocidad de la particula, tanto en x como en y, para que la partícula rebote cuando toque el borde de la pantalla. 

### dibujar(pantalla)
En este método, lo que hacemos es tomar cada uno de los valores dentro de la lista que definimos antes para la forma de la partícula y asignarle una figura creada con pygame. Para el circulo, tomamos la posición inicial (x, y) como el centro del circulo y le damos un radio aleatorio para crear la partícula en forma de circulo. Para el cuadrado, del igual forma tomamos el mismo centro y definimos los vertices del cuadrado al desplazarnos de ese centro cierto radio, por lo cual también es necesario definir el tamaño que deben tener los lados. Por último, para el triangulo, lo que se hace es se calculan los tres vertices en base al centro y a la altura proporcional al radio. 

### generar_colo_aleatorio()
Los colores RGB se escriben como [1, 1, 1] donde cada número corresponde a una tonalidad de Rojo, Verde y Azul, para que la mezcla de estos nos de un nuevo color. Lo que hace esta parte del código, es darnos tres números aleatorios entre 0 y 255 para crear una combinación de colores. Es importante notar que llamamos algunso parámetros de config para dar el valor y mínimo de los colores. Dentro del archivo de config, el valor mínimo es [0, 0, 0] que corresponde al negro y el [255, 255, 255] que corresponde al blanco. 

## 2.4 Simulacion

Dentro de este código, están la funciones que van a determinar el comportamiento de las particulas que creemos. Para ellso definimos las siguientes funciones 

### aplicar_gravedad(particulas)
Esta función primero recibe una lista de objetos llamada **particulas**, luego tenemos un doble **for** para comparar cada par de particulas. Es decir que se hace una comparación entre la partícula a con la b y si estas son la misma (i==j), se salta para no calcular autogravedad. Luego de estos, se calculan las distancias entre las particulas donde dx, dy son las diferencias de posición y luego usamos la raíz cuadrada para calcular la distancia euclidiana. 

La parte de **if distancia == 0**, evita errores su dos partículas están exactamente en el mismo punto. Luego definimos la fuerza gravitatoria, esto se hace usando la ecuación de gravitación universal. En esta parte podemos notar que se usa de nuevo un parámetro de config (config.G), el cual nos va a dar un valor para la constante de gravitación, la cual puede ser editada por el usuario.

Luego, a partir de esta fuerza gravitacional que calculamos, podemos hallar la aceleración (ax, ay) que producen las partículas entre si. Usando esta aceleración, vamos a actualizar la velocidad de cada una de las partículas mediante **a.vx += ax**

### fusionar(particulas)
El objetivo principal de este proyecto, es crear un sistema de particulas que interaccionen entre si, por lo cual vamos a crear una funsión que haga que estas partículas se fusionen cuando estas estén a cierta distancia entre ellas. Esta función crea una lista vacía llamada nuevas, donde vamos a guardar la información de las nuevas partículas. la parte de skip es un conjunto que guarda los índices de partículas ya fusionadas (para no contarlas 2 veces).

Esta función se ejecuta de la siguiente forma:

- Recorre cada par de partículas en la lista.
- Calcula la distancia entre ellas.
- Si están más cerca que un valor mínimo (`config.FUSION_DIST`), **se fusionan**:
  - Se suman sus masas.
  - Se calcula una nueva posición como el **centro de masa**.
  - Se calcula la nueva velocidad como una **media ponderada** (conservando el momento).
  - Las dos partículas originales se eliminan y se reemplazan por una sola.

Los requisitos para esta función es la clase Prticula, los atributos de posición (x, y), velocidad (vx, vy) y masa. Además, de nuevo usamos el archivo config para obtener el parámetro FUSION_DIST.

## 3. tests.py 

Este archivo define pruebas unitarias para validar el funcionamiento de algunos módulos del simulador de partículas, incluyendo la generación de masas y posiciones aleatorias, así como el comportamiento físico de las partículas (como el rebote en los bordes).

Las pruebas están organizadas usando la biblioteca estándar `unittest` de Python. El archivo contiene dos clases de prueba principales:

### 1. `TestGenerador`

Prueba los métodos estáticos de la clase `Generador`, encargada de crear masas y posiciones aleatorias para las partículas.

#### `test_generar_masa_aleatoria`
- Ejecuta la función `generar_masa_aleatoria()` múltiples veces.
- Comprueba que:
  - La masa generada es siempre positiva.
  - La masa está dentro de un rango aceptable (media más tres desviaciones estándar).

#### `test_generar_posicion_uniforme`
- Ejecuta la función `generar_posicion_uniforme(ancho, alto)` múltiples veces.
- Comprueba que:
  - La posición `x` está entre el margen y el ancho menos el margen.
  - La posición `y` está entre el margen y el alto menos el margen.

Estas pruebas aseguran que los generadores de masas y posiciones respetan los límites definidos por el entorno de simulación.

---

### 2. `TestParticula`

Prueba el comportamiento dinámico de una partícula individual.

#### `setUpClass` y `tearDownClass`
- Inicializa y cierra Pygame antes y después de ejecutar las pruebas.
- Se usa una superficie de Pygame (`Surface`) para simular una pantalla sin necesidad de mostrarla gráficamente.

#### `test_rebote_bordes`
- Crea una partícula que empieza cerca del borde superior izquierdo con una velocidad negativa.
- Llama al método `actualizar_pos()` para que la partícula se mueva.
- Verifica que:
  - La partícula rebota dentro de los límites (no sale de la pantalla).
  - La dirección de la velocidad cambia al rebotar (ahora debe ser positiva o nula).

## 4. Config

Este archivo contiene **parámetros globales** utilizados por otros módulos del proyecto de simulación de partículas. Centraliza las constantes necesarias para controlar la simulación, facilitando su mantenimiento, ajuste y comprensión.

El objetivo de `config.py` es actuar como un **centro de configuración** donde se definen todos los valores importantes que controlan:

- El tamaño de la pantalla.
- La cantidad y características de las partículas.
- Las constantes físicas como la gravedad y la distancia de fusión.
- Los rangos de color y masa.

Esto permite modificar el comportamiento de la simulación sin necesidad de editar múltiples archivos del código fuente.


## 5. main.py

Este proyecto es una **simulación visual de partículas bajo la influencia de la gravedad**, desarrollada en **Python con Pygame**. Las partículas tienen masas generadas aleatoriamente y posiciones iniciales distribuidas uniformemente. Cuando se acercan lo suficiente, se **fusionan**, simulando un comportamiento similar al de cuerpos celestes.

La estructura de este código hace lo siguiente:

1. **Inicializa Pygame** y configura la ventana según los valores definidos en `config.py`.
2. **Genera partículas**:
   - Posiciones aleatorias (distribución uniforme).
   - Masas aleatorias (según una distribución gaussiana definida).
   - Velocidades iniciales aleatorias.
3. **Simula gravedad** entre todas las partículas: calcula y aplica fuerzas gravitacionales.
4. **Actualiza posiciones** y **dibuja las partículas** en cada fotograma.
5. **Fusiona partículas** si se encuentran suficientemente cerca.
6. **Mantiene el bucle** hasta que el usuario cierra la ventana.

## 6. makefile


Este archivo `Makefile` está diseñado para automatizar tareas comunes en un proyecto Python que utiliza un entorno virtual y ejecuta una simulación gravitacional con Pygame. Está adaptado para ejecutarse en sistemas **Windows** usando `cmd`.

---

El objetivo principal es simplificar y automatizar tareas como:

- Crear y activar un entorno virtual (`.venv`).
- Instalar dependencias del archivo `requirements.txt`.
- Ejecutar pruebas unitarias.
- Verificar tipos estáticos con `mypy`.
- Ejecutar el script principal de simulación (`main.py`).
- Mostrar un banner decorativo para la terminal.

---

| Regla            | Descripción                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `build`          | Ejecuta todas las tareas: `banner`, `create`, `install`, `test`, `typecheck`, y `run_simulacion`. |
| `banner`         | Muestra un banner ASCII en la terminal.                                     |
| `create`         | Crea un entorno virtual en la carpeta `.venv`.                              |
| `install`        | Instala las dependencias listadas en `requirements.txt`.                    |
| `run_simulacion` | Activa el entorno virtual y ejecuta `main.py`.                              |
| `typecheck`      | Ejecuta `mypy` sobre `main.py` y el módulo `processing/`.                   |
| `test`           | Ejecuta pruebas unitarias desde el directorio `tests/`.                     |

---


Este Makefile está pensado para ser usado desde la terminal de Windows (`cmd`) con la herramienta `make` instalada (puedes usarla con entornos como Git Bash o instalarla manualmente).

## 7. Requirements.txt

Este archivo contiene las dependencias necesarias para ejecutar y desarrollar el proyecto de simulación gravitacional con Python y Pygame.




