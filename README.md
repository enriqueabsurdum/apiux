# Prueba práctica con DRF

Desarrollo de prueba práctica para proceso de selección en APIUX, utilizando el framework Django.

## Despliegue

Clonar o descargar proyecto:

- Para **clonar** utilizar `git clone git@github.com:enriqueabsurdum/apiux.git`.
- En caso de preferir **descarga**, descomprimir archivo una vez finalizada.

Para el desligue local, se recomienda:

1. Dentro de la carpeta del proyecto crear un **entorno virtual** con `python -m venv .env`.
2. Activar entorno virtual `source .env/bin/activate` (En caso de utilizar un sistema operativo distinto a los basados en UNIX/Linux consultar la documentación oficial en [Creación de entornos virtuales](https://docs.python.org/es/3/library/venv.html)).
3. Una vez que el entorno virtual este activado, instalar los **requerimientos del proyecto** mediante `pip install -r requirements.txt`.
4. Ejecutar **migraciones** pendientes de los modelos `python manage.py migrate`.
5. Por último, ejecutar el **servidor local** con `python manage.py runserver`.

Abra un navegador web y acceda a la siguiente URL `http://localhost:8000/api` que mostrará la API navegable provista por Django REST framework.

## API endpoints

El proyecto cuenta con los siguientes *endpoints*:

| Método | Endpoint                   | Descripción                                                  |
| ------ | -------------------------- | ------------------------------------------------------------ |
| POST   | `{url}/api/autor/`         | Crear un **autor** con *nombre* y *nacionalidad*.            |
| GET    | `{url}/api/autor/`         | Retorna una lista de todos los **autores** con sus respectivos **libros**. |
| GET    | `{url}/api/autor/<int:id>` | Retorna un **autor** basado en su *id* con sus respectivos **libros**. |
| POST   | `{url}/api/libro/`         | Crea un **libro** con *título* y asociado al *id* del **autor**. |
