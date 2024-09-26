# Descargar la imagen de ubuntu
FROM ubuntu:22.04

# Actualizar la lista de actualizaciones
RUN apt-get update --fix-missing

# Actualizar la imagen
RUN apt-get upgrade -y

RUN apt-get install python3 -y

# Copiar la carpeta webapp
COPY ./webapp /home/webapp

# Establecer directorio de trabajo
WORKDIR /home/webapp

# Instalar pip
RUN apt-get install python3-pip -y

# Instalar las librerias
RUN pip3 install -r requirements.txt

# Abrir el puerto 8080
EXPOSE 8080

# Ejecutar la aplicacion
CMD [ "python3", "app.py"]