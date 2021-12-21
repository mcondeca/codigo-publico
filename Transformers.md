# Transformers
_Por_: **_Oscar Correa_**

Para algunos modelos de machine learning, el objetivo es recordar que ocurrió en el pasado para predecir el futuro. Por ejemplo, en procesamiento de lenguaje natural, existen tareas de clasificación de texto en las cuales es necesario establecer relaciones entre palabras o frases que aparecen en distintas partes dentro del texto. Es decir, es importante "recordar" de qué se habló al inicio del texto y su relación con la parte intermedia y/o final del mismo párafo o párrafos posteriores. Un modelo que lo logró con mucho éxito es _Seq2Seq_. Sin embargo, a pesar de su éxito, este modelo tiene algunas limitaciones. Internamente, _Seq2Seq_ está conformado por un encoder y un decoder (en ese orden). Ambos componentes son redes neuronales recurrentes llamadas LSTMs. Este tipo de redes procesan cada palabra dentro de un texto de manera secuencial. Esto significa que es muy difícil paralelizar su entrenamiento (utilización de GPUs está limitada). Por otro lado, _Seq2Seq_ puede procesar inputs de variada longitud. Sin embargo, el vector intermedio que se pasa desde el encoder al decoder es de longitud fija, por lo que, cuando el input es un texto muy grande, este vector intermedio no es capaz de capturar toda la información y por lo tanto hay pérdida de información.

## Transformer
En el transformer también existen encoder y decoder. Sin embargo, no es un solo encoder y un solo decoder, sino un stack de encoders conectado a un stack de decoders. En el transformer, por un lado, se procesan las palabras de un texto de manera paralela y, por otro lado, el vector intermedio entre el stack de encoders y el de decoders no es único sino es un conjunto de vectores. Estas características no sólo evitan el procesamiento secuencial del texto de entrada y la pérdida de información, sino que además permiten la aplicación de paradigma de atención.

El paradigma de atención trata de identificar, dentro de este conjunto de vectores enviado desde los encoders a los decoders, el vector que más importancia tiene a la hora de decodificar.

Entrenar un transformer es complicado. Actualmente grandes empresas realizan el entrenamiento. Por ejemplo, _BERT_ es un transformer de Google con enmascaramiento y que para su entrenamiento se utilizó la información de Wikipedia y otros corpus gigantes. Existen varias formas de entrenar un transformer, una de ellas es enmascaramiento. En el enmascaramiento, la idea es predecir palabras, que fueron enmascaradas aleatoriamente, con base en la frase que la precede. En _BERT_, el entrenamiento es bidireccional, es decir, no solo se busca predecir palabras enmascaradas posteriores a una frase, sino también anteriores.

Si bien es cierto que entrenar un transformer es complicado, la verdadera utilidad de este modelo radica en la posibilidad de hacer _transfer learning_. Transfer learning es una técnica que permite utilizar un modelo entrenado sobre conjuntos de datos masivos y que luego es re-entrenado para resolver problemas parecidos utilizando conjuntos de datos más pequeños. En este caso, el modelo que es re-entrenado (afinado) es el transformer.

La presentación en el siguiente link explica el transformer con un ejemplo de traducción de una frase a otro idioma [link de la presentación](https://pichincha.sharepoint.com/:v:/s/ChapterAdvancedAnalytics/EaToAX4BuoNKkshru2eA96kB7h1uEcnFIq6cTeCDD_qWdQ?e=hm3ATP)

## Ejemplo
El ejemplo dentro de este repositorio corresponde a clasificación de texto. Para el efecto, se afinó la versión en español de _BERT_, conocida como _BETO_. Más información acerca de BETO está disponible en https://github.com/dccuchile/beto

El conocimiento del lenguaje español capturado por _BETO_ es “transferido” al modelo de ejemplo, en el que únicamente se requiere afinarlo. El proceso de afinamiento consiste justamente en la inclusión de un clasificador, y en el re-entrenamiento supervisado sobre un dataset más pequeño. De esta manera, el modelo adquiere conocimiento específico del dominio.

El modelo de ejemplo fue entrenado para clasificar cada texto en una o más clases.
