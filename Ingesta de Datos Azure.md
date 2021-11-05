# Ingesta de datos Azure 
El objetivo de este espacio es indicar los pasos a seguir para realizar la ingesta de datos en Azure, la misma que sera consumida desde Databricks por 
los cientificos de datos para la elaboracion de los modelos.

## Requisitos
  Tener acceso a la plataforma Azure
  Azure Portal: es una consilta en donde se puede administrar todos los recursos de Azure
  Azure Data Factory: permite crear pipelines de datos
  Azure Devops: para pasar a producción los pipelines de datos
  
## Pasos a Seguir
1. Los datos para realizar la ingesta deben estar en un repositorio específico, designado por el área de Arquitectura de información 
2. Se debe contar con las aprobaciones respectivas del área de Seguridad , asi como de Gobierno de datos para la ingesta de la informacion a Azure
3. Correr Pipeline de Ingesta en Azure Data Factory


### Aprobaciones de Expertos
 
### Revisión con Gobierno de Datos
    El area de Gobierno de Datos es la encargada de definir la sensibilidad de cada campo que se requiera subir a Azure, por ejemplo el dato de Saldo Cartera 
    del cliente tiene sensibilidad alta, el campo Edad tiene sensibilidad media, etc.
    
### Revisión con Seguridad de la Información
  El area de Seguridad de la informacion es la encargada de dar recomendaciones en funcion de la sensibilidad definida por el area de Gobierno de Datos para
  cada uno de los campos que se va a subir a Azure, asi por ejemplo en el caso de un campo con sensibilidad alta, se define que el dato debe subirse de manera 
  encriptada.

### Azure Devops
  Una vez se haya revisado con los expertos cada uno de los campos a ingestar a Azure, se debe crear un flujo de aprobación en Azure Devops, en el cual se 
  debe especificar los campos que se desean subir a Azure y realizar el pull request del cambio al ambiente de Desarrollo.
  
  Una vez realizado el pull request, se envia automaticamente una notificacion a los diferentes expertos para su revisión y aprobación
  
  Este flujo debe ser revisado y aprobado por el Experto de Ingenieria de Datos, experto de Arquitectura, experto de Seguridad y el experto de Gobierno de Datos
  una vez que se tiene todas estas revisiones,se puede correr el pipeline para la Ingesta de Datos
  
### Pipeline de Ingesta de Datos
 Cuando ya tenemos todas las aprobaciones, se debe correr el pipeline para ingesta de datos en Data Factory, cuando haya finalizado la ejecucion del pipeline se tiene
 lista la data para el consumo por los cientificos de datos .
 
 Para el paso a Producción del piepeline se debe generar otro Pull Request , el cual involucra nuevas aprobaciones.

  
    



