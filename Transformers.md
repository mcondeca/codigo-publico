# Transformers
_Por_: **_Oscar Correa_**

Para algunos modelos de Machine Learning el objetivo es recordar que ocurrió en el pasado para predecir el futuro, existen algoritmos que reciben información en forma de texto y audio, lo analiza y predice, y su resultado es en el mismo formato de entrada.
Un ejemplo es el algoritmo _"Seq2Seq Model within NTM"_ que es un modelo de estructura Encoder (codificador) - Decoder (decodificador). El codificador convierte una secuencia de entrada de longitud variable en un vector de longitud fija y el decodificador decodifica este vector de longitud fija en una secuencia de salida de longitud variable.
Existen inconvenientes en los algoritmos de este tipo, dado que se realiza de forma secuencial los procesos, presenta pérdida de información y el gradiente de optimización va desapareciendo, para resolver estos inconvenientes se genera un Transformers o Transformador.

##### Transformador
El Transformador permite paralelizar el problema, utilizar un conjunto de codificadores y un conjunto de decodificadores que se procesan de manera independiente.
Entrenar un transformador es complicado, actaulamente grandes empresas realizan el entrenamiento, por ejemplo, "BERT" es un transformado de Google con mascaramiento y utilizo la información de Wikipedia como base de entrenamiento, de forma bidireccional; la idea es predecir una palabra con las palabras anteriores y posteriores de los párrafos y este transformados es público. Sus aplicaciones son traductores, responder preguntas de un texto, entre otras.

##### links de accesos
En la presentación realiza la explicación del Transformador con un ejemplo de traducción de una frase a otro idioma, para mayor aprendizaje ingrese al [link de la presentación:](https://pichincha.sharepoint.com/:v:/s/ChapterAdvancedAnalytics/EaToAX4BuoNKkshru2eA96kB7h1uEcnFIq6cTeCDD_qWdQ?e=hm3ATP)

