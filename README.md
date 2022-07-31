## Build the Dockerfile via docker-compose

docker-compose build

## To run the app services via docker compose and also pass flake8

### --rm means remove the container once it is stopped

### sh -c "flake8" run the linter via the shell

docker-compose run --rm app sh -c "flake8"

### create the Django via docker compose

docker-compose run --rm app sh -c "django-admin startproject app ."

### run our services

docker-compose up

###
