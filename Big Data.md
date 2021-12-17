# ¿Quiéres iniciar en el mundo del Big Data?


Por: Estefanía Lozano

“Cuando desarrollé mi primer proyecto de investigación usando análisis de grafos, tenía una laptop con memoria de 8GB y un procesador i7. 
Mi intención era comparar distintas métricas de centralidad para determinar si un usuario en Twitter podía ser catalogado como “influyente”.
Al ejecutar mi código en Python, y dependiendo del algoritmo usado, mi computadora demoraba días, lo cual era improductivo y hasta distractor, 
con esta y otras más experiencias, empecé a entender el beneficio de la computación distribuida y de la importancia de un framework de computo 
que nos permita paralelizar tareas al realizar un análisis de datos” (Lozano, Estefanía) 


Para esto, ¡Llega Apache Spark!


Apache Spark es un engine rápido, creado con el propósito general para el 
procesamiento distribuido de datos a gran escala, o tal como lo conocen como un 
“Buzzword” el Big Data. Además, cuenta con un API que puede ser usado si programas en R, en Python y en Scala. 
Spark provee un stack de 4 librerías construídas sobre su core, y donde su abstracción fundamental es el “Resilient Distribute Datasets” (RDDs)



•	Spark SQL: Trabaja con datos estructurados

•	Mlib: Soporta Machine Learning escalable

•	Spark Streaming: Aplicaciones para el procesamiento de datos en tiempo real

•	GraphX: Trabaja con grafos y procesamiento paralelo de Grafos


<p align="center">
<img 
width="600" 
     alt="bigdata1" 
     src="https://user-images.githubusercontent.com/94183717/145051637-1ffc6c20-c586-4e84-8d94-cb05519c7262.png">


Deteniéndonos en la primera librería de esta herramienta Spark SQL, los beneficios que tendrá un ingeniero, analista o científico de datos son:

  
a.	Importar datos relacionales desde archivos de tipo Parquet, Hive Tables, otros
  
b.	Ejecutar” querys” sobre los datos importados en Dataframes
  
c.	Escribir los datos a archivos Parquet, Hive Tables, otros
  
  


Lo cual hace muy versátil la herramienta, al trabajar con diferentes tipos de archivos y de compresión.

  
Y si te estas preguntando, ¿Cómo puedo probar Spark?


¡Es super fácil! Los creadores de Spark crearon la plataforma Databricks, y no podía faltar la versión Community, 
si deseas crearte una cuenta para comenzar prueba ingresando a este (link)[https://community.cloud.databricks.com/login.html].

Si todo sale bien, deberías ingresar al home de Databricks y ver algo como esto:

<p align="center">
<img width="700" 
     alt="bigdata2" 
     src="https://user-images.githubusercontent.com/94183717/145052510-6716f384-be64-4cdf-a4be-8890b2de7036.png">

  
¡Anímate y usa las ventajas de spark para tu proyecto!


