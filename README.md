# AGRO_WEB
Proyecto para la materia integrados II

Instalar postgres
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' --> primero
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update --> Actualiza el apt-get
sudo apt-get install postgresql-10 --> instala postgres

comandos y manejo basico de postgres

sudo service postgresql start ---> iniciar servicio de postgres
sudo service postgresql status ---> mirar el si esta activo o no postgres
sudo service postgresql stop ---> parar el servicio de postgres

sudo -u postgres psql --> abrir el terminal de postgres
CREATE DATABASE mydatabase; --> crear la base de datos
SELECT usename FROM pg_user; --> Para ver todos los usuarios existentes en PostgreSQL
SELECT * FROM pg_shadow WHERE usename='<username>'; --> ara ver la contraseña de un usuario específico, esta incriptada
ALTER USER <username> WITH PASSWORD '<new_password>'; ---> cambiar la contraseña de un usuario

\l --> listar todas las bases de datos
\q --> salir de la terminal de postgres
\c nombre_de_tu_base_de_datos --> entrar a la base de datos
\dt --> listar las tablas de la base de datos
\d nombre_tabla --> ver en detalle la tabla
SELECT * FROM nombre_de_la_tabla; --> ver los datos de una tabla
:q --> para salir de una tabla si estan viendola en detalle