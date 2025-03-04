import requests
import os

# Configuración de Grobid
grobid_url = "http://localhost:8070/api/processFulltextDocument"

# Rutas
pdf_dir = "/home/javi/Escritorio/ciencia_abierta/articulos_cientificos"
output_dir = "/home/javi/Escritorio/ciencia_abierta/resultados/XML_articulos"

# Función para procesar un PDF
def process_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        files = {'input': (os.path.basename(pdf_path), f, 'application/pdf')}
        response = requests.post(grobid_url, files=files)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al procesar {pdf_path}: {response.status_code}")
        return None

# Procesar todos los PDFs en la carpeta
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        xml_content = process_pdf(pdf_path)

        if xml_content:
            output_filename = os.path.splitext(filename)[0] + ".xml"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write(xml_content)
            print(f"XML guardado en {output_path}")
