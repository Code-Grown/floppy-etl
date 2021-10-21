# Floppy ETL

```
  █████▒██▓     ▒█████   ██▓███   ██▓███ ▓██   ██▓   ▓█████▄▄▄█████▓ ██▓    
▓██   ▒▓██▒    ▒██▒  ██▒▓██░  ██▒▓██░  ██▒▒██  ██▒   ▓█   ▀▓  ██▒ ▓▒▓██▒    
▒████ ░▒██░    ▒██░  ██▒▓██░ ██▓▒▓██░ ██▓▒ ▒██ ██░   ▒███  ▒ ▓██░ ▒░▒██░    
░▓█▒  ░▒██░    ▒██   ██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒ ░ ▐██▓░   ▒▓█  ▄░ ▓██▓ ░ ▒██░    
░▒█░   ░██████▒░ ████▓▒░▒██▒ ░  ░▒██▒ ░  ░ ░ ██▒▓░   ░▒████▒ ▒██▒ ░ ░██████▒
 ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ▒▓▒░ ░  ░▒▓▒░ ░  ░  ██▒▒▒    ░░ ▒░ ░ ▒ ░░   ░ ▒░▓  ░
 ░     ░ ░ ▒  ░  ░ ▒ ▒░ ░▒ ░     ░▒ ░     ▓██ ░▒░     ░ ░  ░   ░    ░ ░ ▒  ░
 ░ ░     ░ ░   ░ ░ ░ ▒  ░░       ░░       ▒ ▒ ░░        ░    ░        ░ ░   
           ░  ░    ░ ░                    ░ ░           ░  ░            ░  ░
                                          ░ ░                               
```

Micro marco de trabajo extensible, adpatable, configurable y sencillo para generar ETL, indicadores o acciones diversas automatizadas bajo el uso de crontabs o bajo demanda.

Los aspectos considerados son:
- [x] Crear sistema automatizado para manejo de datos diariamente.
- [x] Robot con tareas y procesos registrados en la tabla de cronjobs en horarios específicos.
- [x] Generar una serie de argumentos específicos para la extracción a través de comandos (argumentos) parametrizables o directos.
- [x] Orden y estructura mantenible.
- [x] División de responsabilidades por comando.

Plataforma, Framework o Lenguajes de Programación/BBDD y Requisitos:
- [x] Python 3.9.7^
- [x] MongoDB *3.x^
- [x] Mysql *5.7.x^
- [x] PostgreSQL *11.x^
- [x] Docker y Docker Compose
- [x] Crear una copia del archivo .env para crear el .env.dev o .env.prod (variables de entorno) proveída por el desarrollo
- [x] Tener corriendo en una instancia local la base de datos Mysql, Mongo, PostgreSQL ó a través de una conexión remota (vps, servidor, rds, etc)

Configurar variables de entorno:

Solo las variables de entorno marcadas con (*) son las requeridas para desplegar este proyecto, las demás son opcionales en caso de requerir aplicarlas, solo se exponen para promover un formato similar para el uso de estas variables en el proyecto.

------------------------------------
#### Variables de Entorno
```
## FRAMEWORK APP

APP_NAME=application.py
DEBUG=True
THREADED=True
TOKEN=t0k3n4l34t0r10
TZ=America/Santiago
TIMEZONE=America/Santiago
LOCALE=America/Santiago
FALLBACK_LOCALE=America/Santiago
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
ARGUMENTS_DIR_MODULE="arguments"
PARSER_ARGUMENT_DESCRIPTION="Floppy ETL"
DUMP_PARENT_PATH="/app/storage/dumped"
LOG_PATH="/app/storage/logs"
EMAIL_REPORT_TO="esteban@codegrown.cl" # <- Examples

DEFAULT_LOG_CHANNEL=custom
DEFAULT_DB_CONNECTION=mongodb


## MYSQL DATABASE CONNECTION
DBMY_CONNECTION_DRIVER=mysql
DBMY_HOST=productionhost
DBMY_PORT=3306
DBMY_DB=database
DBMY_USER=userrepo
DBMY_PASSWORD=p455w9rd


## POSTGRES DATABASE CONNECTION
DBPG_CONNECTION_DRIVER=postgres
DBPG_HOST=productionhost
DBPG_PORT=5432
DBPG_DB=database
DBPG_USER=userrepo
DBPG_PASSWORD=p455w9rd


## MONGO DATABASE CONNECTION
DBM_CONNECTION_DRIVER=mongodb
DBM_USER=user
DBM_PASSWORD=p455w0rd
DBM_HOST=mongohost
#DBM_HOST=mongohost1,mongohost2,mongohost3 # <- In case of replicaset
DBM_REPLICASET=ReplicaName
DBM_DB=dbname
DBM_PORT=27000
DBM_AUTH_SOURCE=admin
DBM_AUTH_MECHANISM=SCRAM-SHA-1

## MONGO DATABASE WITH ATLAS CONNECTION STRING
# If you have connection string, the connection automatically use setted connection string and try connect
DBM_CONNECTION_STRING=mongodb+srv://<username>:<password>@hostname/database?retryWrites=true&w=majority


```

Deploy Local con Docker Compose
------------------------------------
En el directorio del proyecto, en donde se encuentra el archivo docker-compose.yml, existen 2 servicios creados, el de Desarrollo Local y Producción.

### Ojo: Debes tener instalado docker y docker-compose en tu maquina local

Puedes crear los siguentes aliases en tu archivo ~/.bashrc o ~/.zshrc para simplificar la ejecución:

```
alias dc='docker-compose'
alias dce='docker-compose exec'
alias dcl='docker-compose logs'
alias dclf='docker-compose logs -f'
alias dcup='docker-compose up'
alias dcdown='docker-compose down'
alias dcstop='docker-compose stop'
```

Para poder levantar el ambiente local solo debes ejecutar la siguiente instrucción y esperar que se instalen las dependencias configuradas en el dockerfile que tiene asociado dicho ambiente.

Ejecutando docker compose para enviarlo a background directamente y ver los logs después de su ejecución:

```
docker-compose up --build floppy_etl_dev -d && docker-compose logs floppy_etl_dev -f
```

Ejecutando docker compose para quedar con un watcher de los logs (Ojo al presionar ctrl + c se detiene el servicio, se recomienda dejar la ejecución en background y luego monitorear los logs):

```
docker-compose up --build floppy_dev_dev
```

Para ingresar al contendor desde el directorio del proyecto basta ejecutar la siguiente instrucción:

```
docker-compose exec -u0 floppy_dev_dev bash
```
------------------------------------