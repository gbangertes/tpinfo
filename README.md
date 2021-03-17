# TPInfo - Proyecto final Informatorio

Blog de noticias

## Pre-requisitos 📋

Para probar el proyecto es necesario tener instalado Django 3.1 y MySQL.

Librerías necesarias:
* Pillow
* django-filter
* mysql-client

```
pip install mysql-client Pillow django-filter
```

## Instalación 🔧

Clonar el repositorio, crear el archivo local.py en tpinfo/settings/ con los datos de la base de datos usada.
Migrar los modelos:
```
python3 manage.py migrate
```
Correr el proyecto:
```
python3 manage.py runserver
```

## Construido con 🛠️

* [Django 3.1](https://docs.djangoproject.com/en/3.1/) - Framework
* [MySQL](https://dev.mysql.com/doc/) - Gestor de bases de datos

## Autores ✒️

* **Bangertes, Gabriel** - [gbangertes](https://github.com/gbangertes)
* **Fernandez, Cintia** - [bubacode](https://github.com/bubacode)
* **Linares, Fernando** - [hernanfernandolinares](https://github.com/hernanfernandolinares)

## Licencia 📄

