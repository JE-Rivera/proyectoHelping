# INDICACIONES:

Para poder usar el repositorio, se debe acceder al entorno virtual, primero accede desde la consola al directorio donde descargaste el 
repositorio, luego ingresa el siguiente comando: 

```proyectoHelping\Scripts\activate```

Con este comenado se activa el entorno virtual, con el cual se encapsulan todos los paquetes instalados en el entorno, versiones, etc.
Para usar postgres como base de datos, primero debes ejecutar el siguiente Script desde pgAdminIII, para así crear la base de datos
donde se alamcenaran los datos del sistema:

```sql
CREATE ROLE superUSER LOGIN PASSWORD 'uesFIA2018' VALID UNTIL 'infinity';
CREATE DATABASE helpingDB WITH OWNER superUSER ENCODING='UTF8';
REVOKE CONNECT ON DATABASE helpingDB FROM PUBLIC;
ALTER ROLE superUSER NOINHERIT;```

Ahora, desde la consolo ejecuta el siguiente comando:

```sql
psql -U postgres;```

Ingresas la contraseña que usaste al instalar PostgreSQL en tu PC

El prompt cambiará de la siguiente forma:

```sql
postgres=#```

Ingresas el siguiente comando:

```sql
postgres=# GRANT ALL PRIVILEGES ON DATABASE helpingDB TO superUSER;```
