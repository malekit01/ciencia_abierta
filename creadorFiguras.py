import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Directorios
xml_dir = "resultados/XML_articulos"
output_dir = "resultados/figuras"

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
                xml_content = file.read()
                count = count_figures(xml_content)
                # Obtener solo las primeras 6 letras del nombre del archivo
                short_name = filename[:6]
                article_names.append(short_name)
                figure_counts.append(count)
        except Exception as e:
            print(f"Error al procesar {filename}: {e}")

# Crear la gráfica
plt.figure(figsize=(12, 6))  # Aumentar el tamaño de la figura
plt.bar(article_names, figure_counts)
plt.xlabel("Artículos")
plt.ylabel("Número de Figuras")
plt.title("Número de Figuras por Artículo")
plt.xticks(rotation=45, ha="right", fontsize=8)  # Rotar y ajustar la fuente
plt.tight_layout()# ajustar margenes.

# Guardar la gráfica
output_path = os.path.join(output_dir, "figuras_por_articulo.png")
plt.savefig(output_path)
plt.close()
print(f"Visualización guardada en {output_path}")
