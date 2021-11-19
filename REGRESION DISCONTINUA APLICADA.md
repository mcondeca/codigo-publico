# Aplicación de Regresión Discontinua en los patrones de Oferta Laboral dentro del Hogar

Por: Daniela Santillan 


Las herramientas de política social más populares en países en desarrollo son las transferencias monetarias que son otorgadas
a familias en situación de pobreza para incentivar la inversión en capital humano. Además de los efectos directos, estas transferencias 
monetarias podrían tener otros efectos en los demás miembros del hogar. El estudio busca analizar el impacto de las transferencias monetarias 
del Ecuador en las decisiones de oferta laboral dentro del hogar como efectos causales.


El desafío para estimar efectos causales del impacto de las transferencias monetarias es encontrar variación exógena en la asignación de 
las mismas, que permita identificar su efecto. Una simple comparación entre las personas que reciben y no reciben transferencias monetarias 
noS permite llegar a una inferencia causal, porque los dos grupos tienen diferentes características observables y no observables. Esto genera 
un sesgo de variables omitidas y los resultados pueden atribuir erróneamente un efecto a la transferencia monetaria, cuando el efecto proviene 
de otros factores. Para evitar este problema, se aprovecha de la existencia de un corte en la asignación de las transferencias. Este corte actúa 
como una regla de asignación, en donde los hogares que se encuentran por debajo son elegibles como receptores de las transferencias.
Esta asignación permite estimar el efecto causal del impacto de las transferencias monetarias, utilizando un diseño de regresión discontinua 
difusa. Los datos administrativos provienen de la Unidad de Registro Social y ofrece una oportunidad única de información para las estimaciones, 
falsificaciones y pruebas de robustez que son la base de inferencia causal.


Bajo la metodología propuesta de regresión discontinua difusa se encuentra evidencia de que las transferencias monetarias reducen 
la oferta laboral de los adultos en edad de trabajar por cambios en la oferta laboral en hogares donde viven individuos de 5-14 años, 
25-64 años y más de 65 años. Además, se muestra que no hay cambios importantes en el trabajo infantil, pero sí una disminución en la oferta
laboral de los adultos mayores. Estos hallazgos son particularmente importantes dado los objetivos de diseño de las transferencias monetarias. 


## METODOLOGÍA
## Regresión Discontinua Difusa:


Es una de las herramientas de análisis econométrico de inferencia causal. Ha revolucionado como diseño de experimentos cuasiexperimentales
por la transparencia en supuestos y facilidad en pruebas de robustez. La regresión discontinua es apropiada utilizar en cualquier situación 
en donde la probabilidad en una variable de resultados, por ejemplo, trabajo, salta de manera discontinua ante la existencia de un corte de 
asignación, cuando la unidad de observación está siendo tratada.


El corazón de la regresión discontinua conlleva a que, dado que sabemos que la probabilidad de la asignación de tratamiento cambia de manera 
discontinua en corte, compararemos observaciones por encima y por debajo del corte para estimar un tipo particular de efecto de tratamiento
promedio llamado efecto de tratamiento promedio local, o LATE. Para estimar se usa Two-Stage Least Squares (2SLS) Regression Analysis.


### Links de interés     
Puedes revisar más información sobre el código utilizado en el siguiente  [repositorio](https://github.com/mcondeca/REGRESIONDISCONTINUA)

