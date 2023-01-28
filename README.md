# payments_app
Esta es una aplicación desarrollada con el IDE multiplataforma CLion de JetBrains en lenguaje python orientada a servicios REST con el framework de Django, la función de la misma es obtener cierta información desde API Rest y almacenarla en la base de datos,

### Pre-requisitos 
Se debe descargar el entorno virtual para la descarga de las librerias de la siguiente manera:
1. Se crea el entorno con el comando ``` pip install virtual venv ```
2. Se ejecuta el entorno con el comando ```python -m virtualenv venv ```
3. Se activa el entorno virtual con el comando ```.\venv\Scripts\activate```

En el proyecto se uso JWT, si el entorno virtual no descarga la libreria JWT se descarga con el comando ``` pip install djangorestframework-simplejwt``` , las propiedades ya se encuentran en el archivo ``` settings.py ``` para su uso, para utilizar esta herramienta se creó un usuario por medio del comando ```python manage.py createsuperuser ``` con los datos:
"user : app"
"password : 12345app" 
estos se usan para la validación del token. 

La base de datos usada para este proyecto fue PostgreSQL creando la tabla llamada 'payments'con la siguiente información para la conexión en la base de datos que se indica en el archivo ``` settings.py ``` en la propiedad ```DATABASES```:
se define ``` "ENGINE" ``` para indicar que la base de datos es PostgreSQL, ```  "NAME" ``` para indicar el nombre de la tabla en este caso 'payments', ``` "USER" ``` para usuario en este caso 'postgres', ``` "PASSWORD" ``` para la contraseña definida '1234',
``` "HOST" ``` siendo 'localhost' y ``` "PORT" ``` para el puerto en este caso '5433'.

### Desarrollo del proyecto 
En el proyecto se crearon los modelos para el ingreso de los datos en la APIRest, allí mismo se creó la función ```save()``` en donde se alojó la información que tendran 3 columnas las cuales solo se visualizaran en la base de datos:
1. 'commission_value' : el calculo del valor de la comision del pago.
2. 'card_type' : el tipo de tarjeta de crédito para el que se creo la función ```typecard``` condicionando el tipo por medio de regex.
3. 'response_Payu' : la respuesta del consumo del APIRest que se uso para en ambiente sandbox de PaYu para probar la solución.

Se procede a programar el 'Serializer' para convertir el modelo en un formato serializable para asi programar en 'ViewSet' con el metodo ```ModelViewSet``` para manejar la operaciones CRUD, y allí mismo traemos como atributo en ```serializer_class``` el 'Serializer'
en el archivo ```urls.py ``` de 'projects' se configuran rutas predefinidas que se van a traer en el archivo ```urls.py``` de 'payments_app' en donde también se definen la url para acceder a JWT.

Se creo el archivo ```service.py``` en donde a través de la libreria 'request' se creó una función para consumir la API que proporciona PaYu para ambiente de pruebas de pagos con tarjeta de crédito llamdo sandbox en donde la respuesta del servicio se visualiza en la columna 'response_Payu' 
de la base de datos.

### Pruebas 
Se usó Postman para testear el proyecto y la API de PaYu, los archivos de exportación de estas pruebas se encuentra en la carpeta 'files'.

### Construido con

*Python
*Django
*JWT
*Restframework
*PostgreSQL





