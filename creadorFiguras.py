import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Directorios
xml_dir = "/home/javier/Escritorio/ciencia_abierta/XML_articulos"
output_dir = "/home/javier/Escritorio/ciencia_abierta/figuras"

# Asegurar que el directorio de salida existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def count_figures(xml_content):
    """Cuenta el número de figuras en el contenido XML."""
    try:
        root = ET.fromstring(xml_content)
        figures = root.findall(".//{http://www.tei-c.org/ns/1.0}figure")
        return len(figures)
    except Exception as e:
        print(f"Error al procesar XML: {e}")
        return 0

# Procesar cada archivo XML en la carpeta
article_names = []
figure_counts = []

for filename in os.listdir(xml_dir):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_dir, filename)

        try:
            with open(xml_path, 'r', encoding='utf-8') as file:
