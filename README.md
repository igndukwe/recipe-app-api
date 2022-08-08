## Build the Dockerfile via docker-compose

docker-compose build

## To run the app services via docker compose and also pass flake8

### --rm means remove the container once it is stopped

### sh -c means the shell command we are going to pass in

### sh -c "flake8" run the linter via the shell

docker-compose run --rm app sh -c "flake8"

### create the Django via docker compose

docker-compose run --rm app sh -c "django-admin startproject app ."

### run our services

docker-compose up

# Design Driven Test (DDT)

## 1. Write the test for the behaviour you expect to see in code

## 2. Run out test to Fail

## 3. Write code so that test passes

docker-compose run --rm app sh -c "python manage.py test"
