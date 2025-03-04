import os
import xml.etree.ElementTree as ET
import re

# Directorios
xml_dir = "/home/javi/Escritorio/ciencia_abierta/resultados/XML_articulos"
output_dir = "/home/javi/Escritorio/ciencia_abierta/resultados/links_articulos"

# Asegurar que el directorio de salida existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_links(xml_content):
    """Extrae los enlaces del contenido XML."""
    try:
        root = ET.fromstring(xml_content)
        text_elements = root.findall(".//{http://www.tei-c.org/ns/1.0}p")
        text = " ".join([elem.text for elem in text_elements if elem.text])
        # Expresión regular para encontrar URLs
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        return links
    except Exception as e:
        print(f"Error al procesar XML: {e}")
        return []

# Procesar cada archivo XML en la carpeta
for filename in os.listdir(xml_dir):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".txt")
        
        try:
            with open(xml_path, 'r', encoding='utf-8') as file:
                xml_content = file.read()
            links = extract_links(xml_content)
            
            with open(output_path, 'w', encoding='utf-8') as outfile:
                for link in links:
                    outfile.write(link + "\n")
            
            print(f"Enlaces guardados en {output_path}")
        except Exception as e:
            print(f"Error al leer {xml_path}: {e}")
