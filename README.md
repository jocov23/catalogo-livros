commands to type when initiating the project

#-d == run on background
#--build == rebuild all containers
docker-compose up -d --build == initiate and start all the containers contained in the .yaml file

#if Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:3306 -> 127.0.0.1:0: listen tcp 0.0.0.0:3306: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
try killing each process running in background related to mysql

#if container web command doesn't run automatically(idk why):
docker-compose exec web bash == enter the CLI of the "web" container
python manage.py runserver 0.0.0.0:8000 == start the django application contained in the "web" container


small guide
 =docker-compose.yaml orchestrate the creation of 2 containers: web(django app) and bd(mysql instance)
 =dockerfile is the file which the container web use to its own creation, requirements and .env the same thing
 =urls when activated run a especific function(views) wich can contain CRUD operations or HTML templates
 =views are functions that interact with models
 =models are variables stored in a database through a django-rest-framework
 =serializer convert models to JSON
 =forms are a special class to convert models in HTML
