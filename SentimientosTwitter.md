# Análisis de Sentimiento Financiero en Publicaciones de Twitter


Por: Jorge Barreno


A medida que se intensifica la carrera por generar rendimientos anormales en los mercados de valores, 
muchos inversores buscan fuentes alternativas de información. Recientemente, una de esas fuentes ha sido la masiva 
recopilación de datos de redes sociales que han permitido a varios personas medir el sentimiento acerca de papeles 
comerciales a través del análisis de NLP (Natural Language Processing). Este estudio tuvo como objetivo abordar la clasificación 
de sentimiento de tweets relacionados con finanzas, ya sea como "bullish" (positivo) o "bearish" (negativo).


Se empezó con métodos de machine learning basados en algoritmos de clasificación tradicionales como SVMs con kernels lineales y 
gaussianos, Regresión Logística, y Bernouille Naive Bayes con diferentes técnicas de vectorización, para después utilizar 
modelos de redes neuronales como LSTMs de diferentes tamaños y finalmente modelos BERT pre-entrenados. 


<p align="center">
<img width="600" 
alt="Screenshot 2021-12-21 at 16 21 12" src="https://user-images.githubusercontent.com/94183717/146999328-ea89effe-ce85-40ba-9b73-0c9dec78caab.png">



Twitter es una de las plataformas de redes sociales más grandes del mundo. Los usuarios publican sobre diversos temas, 
y los mercados financieros no son una excepción. Para este estudio se descargaron aproximadamente 200,000 publicaciones de Twitter. 
De las cuales, 100,000 se descargaron buscando la palabra “Bullish” y 100,00 más con la palabra clave “Bearish”. Se tomó la palabra 
clave como la etiqueta de clasificación verdadera para ese post.
Con referencia a los resultados, los modelos de clasificación tradicionales fueron de rendimientos que van de insatisfactorios a decentes en 
relación con la simplicidad y eficiencia de los modelos [57% - 78%]. Sorprendentemente, esto coincide aproximadamente con el bajo rendimiento 
de las distintas redes neuronales LSTM [60% - 68%]. Los ajustes arquitectónicos representaron muy pocos cambios en la precisión del modelo. 
Sin embargo, los modelos BERT basados en transformadores, como el modelo original de Google y el modelo de Araci, FinBERT, arrojaron una precisión 
del 80% en la clasificación del set de prueba. Este rendimiento proviene del aprovechamiento de las capas del transformador BERT para descifrar 
relaciones semánticas.


Se sugiere que de presentase limitaciones en poder o tiempo de computación sería mejor utilizar la regresión logística vectorizada con Tf-Idf, 
o SVM de kernel gaussiano. Si se quiere maximizar la precisión del modelo, se recomienda inequívocamente el uso de modelos de transformadores basados 
en BERT a medida que aprovechan una arquitectura de vanguardia para un rendimiento incomparable. El veredicto sobre el entrenamiento previo adicional 
de BERT con set de datos específicos de dominio, según el experimento, aún no es concluyente.

<p align="center">
<img width="1000" 
     alt="Screenshot 2021-12-21 at 16 21 19" src="https://user-images.githubusercontent.com/94183717/146999444-69dd897c-9fb1-45e0-8811-84450aa7e1e0.png">



