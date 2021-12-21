# Transformers
_Por_: **_Oscar Correa_**

Para algunos modelos de machine learning, el objetivo es recordar que ocurrió en el pasado para predecir el futuro. Por ejemplo, en procesamiento de lenguaje natural (NLP por sus siglas en inglés), existen tareas de clasificación de texto. Para que el resultado de esta tarea sea óptimo, el algoritmo debe ser capaz de establecer relaciones entre palabras o frases que aparecen en distintas partes dentro del texto. Un algoritmo que lo logró con mucho éxito es _Seq2Seq_. Sin embargo, tiene algunas limitaciones. Internamente, _Seq2Seq_ está conformado por un encoder y un decoder (en ese orden). Ambos componentes son redes neuronales recurrentes llamadas LSTMs. Este tipo de redes procesan cada palabra dentro de un texto de manera secuencial. Esto significa que es muy difícil paralelizar su entrenamiento (utilización de GPUs está limitada). Por otro lado, _Seq2Seq_ puede procesar inputs de variada longitud. Sin embargo, el vector intermedio que se pasa desde el encoder al decoder es de longitud fija, por lo que, cuando el input es un texto muy grande, este vector intermedio no es capaz de capturar toda la información y por lo tanto hay pérdida de información.

##### Transformador
El Transformador permite paralelizar el problema, utilizar un conjunto de codificadores y un conjunto de decodificadores que se procesan de manera independiente.
Entrenar un transformador es complicado, actaulamente grandes empresas realizan el entrenamiento, por ejemplo, "BERT" es un transformado de Google con mascaramiento y utilizo la información de Wikipedia como base de entrenamiento, de forma bidireccional; la idea es predecir una palabra con las palabras anteriores y posteriores de los párrafos y este transformados es público. Sus aplicaciones son traductores, responder preguntas de un texto, entre otras.

##### links de accesos
En la presentación realiza la explicación del Transformador con un ejemplo de traducción de una frase a otro idioma, para mayor aprendizaje ingrese al [link de la presentación](https://pichincha.sharepoint.com/:v:/s/ChapterAdvancedAnalytics/EaToAX4BuoNKkshru2eA96kB7h1uEcnFIq6cTeCDD_qWdQ?e=hm3ATP)

