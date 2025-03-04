# Usa una imagen base con Python 3.9
FROM python:3.9-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Haz que el script prev_practica.sh sea ejecutable
RUN chmod +x prev_practica.sh

# Comando para ejecutar el script prev_practica.sh al iniciar el contenedor
CMD ["bash", "prev_practica.sh"]
