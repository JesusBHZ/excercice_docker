# Repositorio de prueba de docker

## Crear imagen 
docker build -t image:tag .

## Correr contenedor
docker run -p 8080:8080 josechuy:1

## Muestra los contenedores inactivos
docker ps -a

## Arranca un contenedores
docker start

## Muestra los contenedores activos
docker ps 

## Muerte al contenedor
docker kill image

## Iniciar contendor en modo interactivo
docker start -i image

## Mostrar imagenes
docker images

## Iniciar sesion
docker login

# Crear etiqueta
docker tag josechuy:1 jesusbhz/dockerprueba:latest

# Subir imagen
docker push jesusbhz/dockerprueba