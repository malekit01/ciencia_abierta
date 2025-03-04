#ciencia_abierta

Este repositorio contiene los contenidos para la práctica de ciencia abierta. Incluye scripts de Python para procesar PDFs de artículos científicos, generar nubes de palabras, extraer figuras y enlaces, así como un script de configuración y un archivo de requisitos.

#Contenido

lectroPDF.py: Script para procesar archivos PDF de artículos científicos utilizando Grobid y convertirlos a formato XML.

creadorNubesPalabras.py: Script para generar nubes de palabras a partir de los archivos XML generados por lectroPDF.py.

creadorFiguras.py: Script para contar el número de figuras en los archivos XML y generar una gráfica comparativa.

extractorLinks.py: Script para extraer enlaces de los archivos XML.

prev_practica.sh: Script de shell para crear la estructura de carpetas necesaria para los scripts.

requirements.txt: Lista de dependencias de Python necesarias para ejecutar los scripts.

LICENSE: Archivo de licencia para el repositorio.

CITATION: Archivo de citación para el repositorio.

#Requisitos

Antes de ejecutar los scripts, asegúrate de tener instalado Python 3 y las siguientes dependencias:

matplotlib
wordcloud
requests
Puedes instalar las dependencias utilizando pip:
