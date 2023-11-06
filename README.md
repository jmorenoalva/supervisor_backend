# Ejercicio práctico de Django

## Instalación:

```
python -m venv venv

# Activación en Unix
source venv/bin/activate

# Activación en Windows
venv\Scripts\activate

pip install -r requirements.txt

make migrate
```

Para crear un super usuario y acceder al admin:

```
make createsuperuser
```

Para levantar el servidor:

```
make run
```

## Base de datos:

Esto proyecto requiere que tenga instalado MySQL.
Actualice los datos de la base de datos en un archivo .env el cual sera llamaro desde `settings/prod.py`.

```
NAME_DATABASE='nombre_base_datos'
USER_DATABASE='usuario'
PASSWORD_DATABASE='password'
HOST='ipolocalhost'
PORT='puerto'
```
