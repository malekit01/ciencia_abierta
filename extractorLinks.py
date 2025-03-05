import os
import re
import xml.etree.ElementTree as ET

# Directorios de entrada y salida
xml_dir = "resultados/XML_articulos"
output_dir = "resultados/links_articulos"

# Crear la carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Expresión regular mejorada para detectar URLs
url_pattern = re.compile(r'https?://[^\s<>"\'()]+')

def extract_links_from_xml(xml_file):
    """Extrae enlaces de un archivo XML y los devuelve en una lista."""
    links = set()  # Usamos un set para evitar duplicados

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Recorrer todos los elementos del XML
        for elem in root.iter():
            # Extraer enlaces de texto dentro de las etiquetas
            if elem.text:
                links.update(url_pattern.findall(elem.text))

            # Extraer enlaces de atributos (como href, src, target, etc.)
            for attr_value in elem.attrib.values():
                links.update(url_pattern.findall(attr_value))

            # Extraer enlaces de "tail" (texto después de una etiqueta)
            if elem.tail:
                links.update(url_pattern.findall(elem.tail))

    except Exception as e:
        print(f"Error procesando {xml_file}: {e}")
    
    return sorted(links)  # Devolver lista ordenada para mejor legibilidad

# Lista para almacenar los archivos generados
archivos_generados = []

# Procesar cada archivo en la carpeta XML
for filename in os.listdir(xml_dir):
    if filename.endswith(".xml"):  # Asegurarse de que es un XML
        xml_path = os.path.join(xml_dir, filename)
        links = extract_links_from_xml(xml_path)

        # Guardar enlaces en un archivo de salida si hay enlaces encontrados
        if links:
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_links.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(links))
            archivos_generados.append(output_path)

# Mostrar un único mensaje con los archivos generados
if archivos_generados:
    print(f"Enlaces extraídos y guardados en {output_dir}")
   
else:
    print("No se encontraron enlaces en ningún archivo.")

