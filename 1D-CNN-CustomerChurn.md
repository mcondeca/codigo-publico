# Redes Neuronales Convolucionales en 1D para predecir la deserción de clientes

El problema de predicción de la Deserción de Clientes o _Customer Churn_ consiste en cuantificar el número de clientes que pueden dejar de consumir un producto o servicio.
Existen varios beneficios de monitorear el Churn, entre ellos está:
1. **Reducción de costos:** el costo de adquirir un nuevo cliente puede ser hasta cinco veces mayor que el costo de retener uno ya existente. 
2. Es más probable que un cliente ya existente **recompre** o se **re-subscriba** al producto
3. La tasa de éxito en ventas es entre un **60% - 70%** en clientes existentes, en comparación al 5% - 20% de tasa de éxito en ventas a clientes nuevos.
4. Es **siete veces más probable** un cliente existente compre o prueve otro de los productos o servicios ofertados por la empresa.
5. Los clientes leales se convierten en embajadores de la marca y por lo tanto, referirán a más personas el producto o servicio y los costos de aquisición disminuirán.

### Redes Neuronales Artificiales
En pocas palabras una red neuronal artificial es un modelo matemático que está inspirado en las células del sistema nervioso de los seres vivos. 

Los componentes básicos que forman a una red neuronal son: las neuronas o nodos y las conecciones. 

El perceptrón de una capa es el modelo de red neural más simple. Como se puede ver en la imagen, la información entra a la red por una única capa [_layer_] de nodos y esta capa de nodos está directamente conectada con el output o el resultado de salida de la red.

<p align="center">
<img 
     src="https://user-images.githubusercontent.com/93781339/145600942-870dec50-9c45-43ed-b0e2-9b00f020e8d6.png"
     alt="SingleLayerPerc"
     style="float: left; margin-right: 5px;" 
     width = "250"
     height = "250"
     align = "center"/>
</p>

Las conecciones entre nodos se ejecutan por medio de funciones o transformaciones matemáticas. Por ejemplo, en el caso de las redes neuronales que se utilizan para las tareas de reconocimiento de imágenes, la capa de entrada a la red se encargas de recibir las imágenes para luego convertir cada una de esas imágenes en una matriz de pixeles. Luego de tener la información en formato de matrices, se aplican funciones conocidas como convoluciones que permiten identificar características en las imágenes como formas, bordes, entre otras.

<!--- Añadir párrafo sobre funciones de activación --->

Añadiendo capas y conexiones a las redes se obtienen modelos más complejos como los que se utilizan para procesamiento del lenguaje natural [_Natural Language Processing_], reconocimiento y clasificación de imágenes, traducción de idiomas, entre otras aplicaciones.

## Redes Neuronales Convolucionales en 1D

Es muy conocida la aplicación de las redes convolucionales en 2 dimensiones para el reconocimiento y clasificación de imágenes, sin embargo también se puede aplicar la misma idea para una dimensión. En este caso, los tensores tienen matrices en 1D, por ejemplo, un conjunto de señales en 1D que son enviadas por un dispositivo. Las convoluciones siguien siendo un producto interno.

Recordemos que una convolución es básicamente una operación matemática donde se suman los productos de una función con otra que ha sido revertida y desplazada. Si _f_ y _g_ son funciones integrables, entonces la convolución de _f_ y _g_ se define por 

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\int_{-\infty}^\infty&space;f(\tau)g(t-\tau)\mathrm{d}\tau" title="\int_{-\infty}^\infty f(\tau)g(t-\tau)\mathrm{d}\tau" 
     width = "150"
     />
</p>

## Aplicación a la predicción de la deserción de clientes

La aplicación de este algoritmo de redes neuronales se hizo utilizando la información de clientes de una conocida empresa de telefonía. La información esta totalmente anonimizada tanto por columnas como registros y en total se tenían 116 variables independientes más la variable _target_.

El conjunto de entrenamiento contenía la información del período de febrero de 2019 y el conjunto de validación tenía información de marzo de 2019.

### Preprocesamiento de los datos
1. La información compartida por la empresa ya había sido transformada y limpiada casi en su totalidad, simplemente se hizo tratamiento de unos cuantos datos nulos.

2. Luego se aplicó un _One-Hot Encoding_ a todas las columnas de tipo categóricas, generando en 135 variables en total para hacer el análisis.

3. Para reducir la dimensionalidad del problema se utilizó primero un algoritmo de _Random Forest_ y se seleccionó las 66 variables con más poder discriminador, las cuales fueron utilizadas luego en la red neuronal

4. La arquitectura de la red neuronal utilizada es la que se muestra en el siguiente gráfico

<p align="center">
<img width="496" alt="image" src="https://user-images.githubusercontent.com/93781339/146573112-814bc55d-3f89-485b-b9ef-fcca6fdf5254.png">
</p>

5. Este ejercicio se llevó a cabo utilizando la plataforma de Watson Studio de IBM, utilizando un kernel con 64GB de memoria RAM y en lenguaje Python. Las principales librerías utilizadas fueron <code>sklearn</code> para el modelo de Random Forest y <code>keras</code> para la red neuronal.

### Resultados Generales
* Este modelo permitió generar una mejora de 5% en la métrica del KS.
* El _Lift_, que se define como el porcentaje acumulado de _churners_ dividido para el porcentaje acumulado del total de clientes, mejoraba en casi 2 puntos en el grupo de donde el modelo predecía la mayor probabilidad.
* Las ganancias acumuladas con la CNN eran mayores que las que se obtenía con el modelo baseline.
## Notebook con código de este proyecto
Puedes revisar más información sobre el código utilizado en el siguiente repositorio [1D CNN model Prediction](https://github.com/raquelvargas16/ibm-projects/blob/master/Churn%201D%20CNN%20model%20(One-Hot%20Encoding).ipynb)

