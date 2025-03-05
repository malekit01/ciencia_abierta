import os
import xml.etree.ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Directorios
xml_dir = "resultados/XML_articulos"
output_dir = "resultados/nubes_palabras"

# Asegurar que el directorio de salida existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_wordcloud(xml_content, output_path):
    """Genera una nube de palabras a partir del contenido XML, filtrando palabras de más de 5 letras."""
    try:
        root = ET.fromstring(xml_content)
        text_elements = root.findall(".//{http://www.tei-c.org/ns/1.0}p")
        text = " ".join([elem.text for elem in text_elements if elem.text])

        # Filtrar palabras de más de 5 letras
        words = [word for word in text.split() if len(word) > 5]
        filtered_text = " ".join(words)

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(output_path)
        plt.close()
        print(f"Nube de palabras guardada en {output_path}")
    except Exception as e:
        print(f"Error al procesar XML: {e}")

# Procesar cada archivo XML en la carpeta
for filename in os.listdir(xml_dir):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")
        
        try:
            with open(xml_path, 'r', encoding='utf-8') as file:
                xml_content = file.read()
            generate_wordcloud(xml_content, output_path)
        except Exception as e:
            print(f"Error al leer {xml_path}: {e}")
