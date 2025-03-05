# Ciencia_abierta

Este repositorio contiene los contenidos para la práctica de ciencia abierta. Incluye scripts de Python para procesar PDFs de artículos científicos, generar nubes de palabras, extraer figuras y enlaces, así como un script de configuración y un archivo de requisitos.
## Contenido

- **lectroPDF.py**: Script para procesar archivos PDF de artículos científicos utilizando Grobid y convertirlos a formato XML.

- **creadorNubesPalabras.py**: Script para generar nubes de palabras a partir de los archivos XML generados por lectroPDF.py.

- **creadorFiguras.py**: Script para contar el número de figuras en los archivos XML y generar una gráfica comparativa.

- **extractorLinks.py**: Script para extraer enlaces de los archivos XML.

- **prev_practica.sh**: Script de shell para crear la estructura de carpetas necesaria para los scripts.

- **requirements.txt**: Lista de dependencias de Python necesarias para ejecutar los scripts.

- **LICENSE**: Archivo de licencia para el repositorio.

- **CITATION**: Archivo de citación para el repositorio.

>**Requisitos**

Antes de ejecutar los scripts, asegúrate de tener instalado Python3 y las siguientes dependencias:

- matplotlib

- wordcloud

- requests

Puedes instalar las dependencias utilizando pip o con el archivo requirements.txt del repositorio como se indica en **Configuracion** en el paso **3**  : 

También necesitas tener Grobid instalado. Puedes encontrar instrucciones de instalación en el repositorio de Grobid (https://github.com/kermitt2/grobid) .

## Configuracion

1. Clona el repositorio

		git clone https://github.com/malekit01/ciencia_abierta
2. accede a la carpeta ciencia_abierta

		cd ciencia_abierta
3. comprobar que las depedencias estan instaladas	

		pip install -r requirements.txt
4. Ejecuta el script prev_practica.sh para crear la estructura de carpetas necesaria

		bash prev_practica.sh
5. Coloca tus archivos PDF de artículos científicos en la carpeta 

	  	/ciencia_abierta/articulos_cientificos
   
	ya hay 10 articulos base que puede usar.

6.  Ejecutar Grobid en otra terminal:
	
		 docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

	si prefieres usar solo una terminal añadir **&** al final del anterior comando 

con estos pasos tendriamos la configuracion previa para poder ejecutar los programas.

## Uso
1. Ejecuta lectroPDF.py para procesar los PDFs y generar archivos XML:

		python3 lectroPDF.py

2. Ejecuta creadorNubesPalabras.py para generar nubes de palabras a partir de los archivos XML:

		python3 creadorNubesPalabras.py

3. Ejecuta creadorFiguras.py para contar figuras y generar una gráfica:

		python3 creadorFiguras.py

4. Ejecuta extractorLinks.py para extraer enlaces de los archivos XML:

		python3 extractorLinks.py

>Licencia

Este proyecto está licenciado bajo la [LICENCIA].

>Citación

Si utilizas este repositorio en tu investigación, por favor cita este trabajo como se describe en [CITATION]

## Notas
- El script **prev_practica.sh** debe ejecutarse antes de cualquier otro script para asegurar que la estructura de carpetas esté configurada correctamente.
- Los scripts asumen que los archivos PDF y XML están en los directorios especificados. Asegúrate de que los archivos existan y estén en los formatos correctos.
- Para un correcto funcionamiento de lectroPDF.py es necesario que Grobid este instalado y en funcionamiento.
