##################

# Docker Compose

##################

## Build the Dockerfile via docker-compose

docker-compose build

### run our services

docker-compose up

### stop all containers services

docker-compose down

## To run the app services via docker compose and also pass flake8

### --rm means remove the container once it is stopped

### sh -c means the shell command we are going to pass in

### sh -c "flake8" run the linter via the shell

docker-compose run --rm app sh -c "flake8"

### create the Django app via docker compose to reside in the current directory

docker-compose run --rm app sh -c "django-admin startproject app ."

### create another Django app called core via docker compose to reside in app directory

docker-compose run --rm app sh -c "python manage.py startapp core"

############################

# Design Driven Test (DDT)

############################

## 1. Write the test for the behaviour you expect to see in code

## 2. Run out test to Fail

## 3. Write code so that test passes

#####################################

# Docker Compose with python commands

#####################################
docker-compose run --rm app sh -c "python manage.py test"

## making a new migration for the database

docker-compose run --rm app sh -c "python manage.py makemigrations"

## migrate you new database

docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

## if migrate does not work properly, we need to delete our previous db

docker-compose down
docker volume rm recipe-app-api_dev-db-data
docker volume ls

## create super user

docker-compose run --rm app sh -c "python manage.py createsuperuser"

Email: admin@example.com
Password: @abcd1234
