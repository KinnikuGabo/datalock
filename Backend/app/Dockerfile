# Utiliza una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY ./app /app

# Copia los archivos clave_secreta.key, key.json y keys.json al contenedor desde el directorio raíz
COPY ../clave_secreta.key /app
COPY ../key.json /app
COPY ../keys.json /app

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Define el comando a ejecutar cuando se inicie el contenedor
CMD ["python", "app.py"]
