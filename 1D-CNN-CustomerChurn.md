# Redes Neuronales Convolucionales en 1D para predecir la deserción de clientes

EL problema de predicción de la Deserción de Clientes o _Customer Churn_ consiste en cuantificar el número de clientes que pueden dejar de consumir un producto o servicio.
Existen varios beneficios de monitorear el Churn, entre ellos está:
1. **Reducción de costos:** el costo de adquirir un nuevo cliente puede ser hasta cinco veces mayor que el costo de retener uno ya existente. 
2. Es más probable que un cliente ya existente **recompre** o se **re-subscriba** al producto
3. La tasa de exito en ventas es entre un **60% - 70%** en clientes existentes, en comparación al 5% - 20% de tasa de exito en ventas a clientes nuevos.
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

Añadiendo capas y conexiones a las redes se obtienen modelos más complejos como los que se utilizan para procesamiento del lenguaje natural [_Natural Language Processing_], reconocimiento y clasificación de imágenes, traducción de idiomas, etcétera.

## Redes Neuronales Convolucionales en 1D

Es muy conocida la aplicación de las redes convolucionales en 2 dimensiones para el reconocimiento de imágenes, sin embargo también se puede aplicar la misma idea para una dimen

## Notebook con código de este proyecto
Puedes revisar más información sobre el código utilizado en el siguiente repositorio [1D CNN model Prediction](https://github.com/raquelvargas16/ibm-projects/blob/master/Churn%201D%20CNN%20model%20(One-Hot%20Encoding).ipynb)

