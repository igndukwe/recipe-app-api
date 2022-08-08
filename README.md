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

# Design Driven Test (DDT)

## 1. Write the test for the behaviour you expect to see in code

## 2. Run out test to Fail

## 3. Write code so that test passes

docker-compose run --rm app sh -c "python manage.py test"
