# Ingesta de datos Azure 
El objetivo de este espacio es indicar los pasos a seguir para realizar la ingesta de datos en Azure, la misma que sera consumida desde Databricks por 
los científicos de datos para la elaboración de los modelos.

## Requisitos
  Tener acceso a la plataforma Azure
  
  Azure Portal: es una consulta en donde se puede administrar todos los recursos de Azure
  https://azure.microsoft.com/es-es/features/azure-portal/
  
  Azure Data Factory: permite crear pipelines de datos
  https://azure.microsoft.com/es-mx/services/data-factory/#overview
  
  Azure Devops: permite pasar a producción los pipelines de datos
  https://azure.microsoft.com/es-es/services/devops/
  
  
## Pasos a Seguir
1. Los datos para realizar la ingesta deben estar en un repositorio específico, designado por el área de Arquitectura de información 
2. Se debe contar con las aprobaciones respectivas del área de Seguridad , así como de Gobierno de Datos para la ingesta de la información a Azure
3. Correr Pipeline de Ingesta en Azure Data Factory


## Aprobaciones de Expertos
Es necesario que la data que vaya a ser ingestada sea revisada por los expertos del área de Gobierno de Datos y de Seguridad de la información

 
## Revisión con Gobierno de Datos
El área de Gobierno de Datos es la encargada de definir la sensibilidad de cada campo que se requiera subir a Azure, por ejemplo el dato de Saldo Cartera 
del cliente tiene sensibilidad alta, el campo Edad tiene sensibilidad media, etc. 

Adicionalmente esta área es la encargada de indicarnos las fuentes certificadas (servidores, base de datos, tablas, filtros)  para la obtención de cada campo.
Existe un experto de datos para cada dominio de la información , se debe realizar una revisión con cada experto de dominio, por ejemplo Dominio Clientes para datos relacionados con clientes, Dominio Canales para datos relacionados con transacciones en canales, Dominio Pasivos para datos relacionados con productos del pasivo, etc

    
## Revisión con Seguridad de la Información

  El area de Seguridad de la información es la encargada de dar recomendaciones en función de la sensibilidad definida por el area de Gobierno de Datos para
  cada uno de los campos que se va a subir a Azure, así por ejemplo en el caso de un campo con sensibilidad alta, se define que el dato debe subirse de manera 
  encriptada.

### Azure Devops
  Una vez se haya revisado con los expertos cada uno de los campos a ingestar a Azure, se debe crear un flujo de aprobación en Azure Devops, en el cual se 
  debe especificar los campos que se desean subir a Azure y realizar el pull request del cambio al ambiente de Desarrollo.
  
  Una vez realizado el pull request, se envia automaticamente una notificación a los diferentes expertos para su revisión y aprobación
  
  Este flujo debe ser revisado y aprobado por el Experto de Ingenieria de Datos, experto de Arquitectura, experto de Seguridad y el experto de Gobierno de Datos
  una vez que se tiene todas estas revisiones, se puede correr el pipeline para la Ingesta de Datos
  
### Pipeline de Ingesta de Datos
Cuando ya tenemos todas las aprobaciones, se debe correr el pipeline para ingesta de datos en Data Factory, cuando haya finalizado la ejecucion del pipeline se tiene lista la data para el consumo por los científicos de datos .
 
 ##
 Para el paso a Producción del pipeline se debe generar otro Pull Request , el cual involucra nuevas aprobaciones.
 

  
    



