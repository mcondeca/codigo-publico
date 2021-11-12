# Midiendo las fluctuaciones de precio en la plataforma Amazon, por medio de dos modelos matemáticos: Maskin Tirole y Sobel Model

Por: Ma. Daniela Conde

<p align="center">
<img 
     src="https://user-images.githubusercontent.com/94183717/141489624-58784301-3d44-4eee-a0d0-1edd7caaa3bb.jpg"
     alt="Amazon"
     style="float: left; margin-right: 5px;" 
     width = "170"
     height = "100"
     align = "center"/>
     

Varios factores pueden atribuirse al éxito de Amazon en el comercio electrónico, incluido un esquema de incentivos para empleados, estrategia 
de marca corporativa y la ventaja de ser el primero. Sin embargo, la literatura apunta a que la estrategia de precio es un factor clave para el éxito de Amazon.
Pero ¿qué impulsa a los distintos algoritmos de precios en Amazon? Los algoritmos de precios dinámicos utilizados por las plataformas podrían analizarse 
utilizando un sin número de modelos, sin embargo, la literatura apunta a dos modelos: Maskin-Tirole y Sobel como los más utilizados.
     

El modelo Maskin-Tirole muestra cómo las estrategias de precios son impulsadas por los precios de otras empresas. En este modelo, dos empresas compiten para vender un producto homogéneo en sucesivos periodos de tiempo. En períodos pares, la empresa 1 puede cambiar su precio. En períodos impares, la empresa dos puede variar su precio.  El equilibrio del juego sigue un camino donde se produce un continuo recorte de precios de ambas empresas hasta llegar al precio más bajo que es el costo marginal del producto, implicando que la probabilidad condicional de subir un precio sea p en cada período; por lo tanto, la duración del recorte de precio se distribuye geométricamente.
     
<p align="center">
<img 
     src="https://user-images.githubusercontent.com/94183717/141491597-bbcb9540-8845-41c0-af86-692d67b8ecea.png"
     alt="MT"
     style="float: left; margin-right: 5px;" 
     width = "700"
     height = "400"
     align = "center"/>
  

El modelo de Sobel tiene como objetivo analizar el lado de la demanda y determinar si el conocimiento de los consumidores y los costos de cambio afectan los precios. Aquí el vendedor de un bien mantiene ventas periódicas como un medio de discriminación de precios. El monopolista se enfrenta a una población de dos tipos de consumidores. El tipo 1 tiene una alta disposición a pagar y poca paciencia, mientras que el tipo 2 tiene una baja disposición a pagar y mucha paciencia. La empresa generalmente establece un precio alto y vende al Tipo 1. Ocasionalmente, reduce el precio para vender a los clientes de Tipo 2 que han estado esperando una venta.  A la luz de esto, se utilizo una duración constante si el tipo de distribución no cambia. En el modelo, todos los consumidores de baja disposición compran en un día de oferta; después de esto se espera que los precios incrementen instantáneamente.  En la distribución de Sobel, se espera que la mayoría de las observaciones tengan una duración de un día. 

<p align="center">
<img 
     src="https://user-images.githubusercontent.com/94183717/141491607-0ed64d5b-c46f-43e6-a7e3-4a02155dba62.png"
     alt="SOBEL"
     style="float: left; margin-right: 5px;" 
     width = "700"
     height = "400"
     align = "center"/>
   

Para analizar estos dos modelos se utilizo una base de datos autoconstruida que contiene cotizaciones de precios que se obtuvieron manualmente de Amazon. Los datos incluyen los precios diarios de 100 productos durante seis semanas (26.12.2020–02.02.2021). Los productos fueron seleccionados al azar usando un generador de números aleatorios Para la prueba de línea base se utilizó un umbral de corte del 25%. Entonces, se formuló la pregunta: para cada ocasión en que el precio cae, ¿Cuántos períodos se necesitan antes de que el precio vuelva a subir? Se calculó el Chi-Cuadrado a tres pruebas diferentes con supuestos clave. 


Para la primera comparación, se asumió que todos los productos de la muestra eran homogéneos. Los resultados mostraron que la distribución de Sobel tenía una mayor correlación entre los valores observados y esperados en la muestra. Se rechazo el modelo Maskin-Tirole y se concluyo que el modelo de Sobel es un candidato razonable para esta prueba.


Para la segunda prueba, se agrupó las 10 categorías en dos grupos principales basados en los principios de marketing de Claessen. Un grupo consiste en los productos que se compran con frecuencia y sin gran comparación, el otro son los productos que los consumidores compran con menos frecuencia y de forma más cuidadosa.  Para esta prueba, la hipótesis es que el modelo de Sobel explica mejor la variación de precios de los productos de menor frecuencia de compra y Maskin-Tirole explicaría los productos comprados con más frecuencia. Los resultados mostraron que, para la categoría de commodities ninguno de los dos modelos se descarta; ambos podrían explicar los datos. Por otro lado, el modelo de Sobel encaja mejor en la categoría de productos con valor añadido porque los productos con una tendencia más baja de compra es probable que se enfrenten a dos tipos diferentes de consumidores: impacientes y pacientes. Finalmente, para la tercera prueba, se permitió una probabilidad diferente para cada producto y solo seis productos mostraron un patrón que podría atribuirse a uno de los dos modelos. 


Al interpretar los resultados, hay que recordar que se basan en una muestra. Es posible que diferentes productos conlleven otros resultados. Y que los resultados actuales provengan de los supuestos usados.  Diferentes patrones de dinámica de precios en Amazon podrían ser analizado por diferentes modelos de los que se analizan en este artículo. El número de observaciones es otra limitación; por eso, para la primera prueba, se asumió homogeneidad entre los productos; sin embargo, esto está lejos de la realidad. Cada uno de los productos analizados son productos diferenciados con los atributos del producto. Para la segunda prueba, la suposición se volvió más flexible y cercana a la realidad; sin embargo, el número de observaciones disminuyo. La tercera prueba solo nos da una imagen de las fluctuaciones de precios de los productos de la muestra durante el tiempo analizado. Esta variación podría explicarse por otros factores exógenos que ocurren al mismo tiempo en el mercado. 


