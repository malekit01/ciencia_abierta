# Rationale: Validación de Resultados

Este documento describe el proceso de validación para cada uno de los scripts desarrollados en este repositorio.

## Configuración del Entorno con `prev_practica.sh`

### Propósito
El script `prev_practica.sh` se utiliza para configurar la estructura de carpetas necesaria para la ejecución de los demás scripts. Este script asegura que todas las carpetas de salida estén creadas antes de ejecutar los scripts principales.

### Validación
1.  **Ejecución del Script:**
    * Se ejecutó el script `prev_practica.sh` en un entorno de Linux/macOS para verificar que se crearan las carpetas correctamente.
    * Se verificó que la carpeta base `ciencia_abierta` y la carpeta de resultados `resultados` se crearan en el directorio `$HOME/Escritorio`.
    * Se verificó que las subcarpetas `figuras`, `links_articulos`, `nubes_palabras`, y `XML_articulos` se crearan dentro de `resultados`.
2.  **Verificación de la Estructura de Carpetas:**
    * Se revisó manualmente la estructura de carpetas creada para asegurar que coincidiera con la estructura esperada.
    * Se verificó que no se generaran errores durante la ejecución del script.
3.  **Independencia del Entorno:**
    * Se ejecutó el script en diferentes entornos de prueba para asegurar que funcionara correctamente independientemente de la configuración previa del sistema.

## 1. lectorDPF.py

### Propósito
Este script utiliza Grobid para convertir archivos PDF de artículos científicos en formato XML.

### Validación
1.  **Verificación de la Instalación de Grobid:**
    * Se aseguró que Grobid estuviera correctamente instalado y funcionando en `http://localhost:8070`.
    * Se realizaron pruebas con PDFs de muestra para confirmar que Grobid respondía correctamente.
2.  **Inspección de la Salida XML:**
    * Se revisaron manualmente los archivos XML generados para verificar la estructura y el contenido.
    * Se comparó el contenido textual extraído con el texto original de los PDFs para asegurar la precisión.
    * Se verifico que los archivos XML se guardaran en la carpeta "resultados/XML_articulos"
3.  **Manejo de Errores:**
    * Se probó el script con PDFs corruptos o no estándar para verificar que el manejo de errores fuera adecuado (impresión de mensajes de error).
    * Se verifico que los archivos que no se pudieron procesar no generaran archivos XML.

## 2. creadorFiguras.py

### Propósito
Este script cuenta el número de figuras en los archivos XML generados por `lectorDPF.py` y crea un gráfico de barras que muestra el número de figuras por artículo.

### Validación
1.  **Verificación del Conteo de Figuras:**
    * Se revisaron manualmente algunos archivos XML para contar el número de etiquetas `<figure>` y se comparó con los resultados del script.
    * Se verificó que el script manejara correctamente archivos XML con diferentes estructuras.
2.  **Inspección de la Gráfica:**
    * Se revisó visualmente la gráfica generada para asegurar que los nombres de los artículos y el número de figuras fueran correctos.
    * Se verificó que la gráfica se guardara correctamente en `resultados/figuras/figuras_por_articulo.png`.
    * Se verifico que los nombres de los archivos en el eje x fueran los 6 primeros caracteres del nombre del archivo xml.
3.  **Manejo de Errores:**
    * Se probó el script con archivos XML corruptos o inexistentes para verificar que el manejo de errores fuera adecuado (impresión de mensajes de error).

## 3. creadorNubesPalabras.py

### Propósito
Este script genera nubes de palabras a partir del contenido textual de los archivos XML, filtrando palabras de más de **5** letras.

### Validación
1.  **Inspección de las Nubes de Palabras:**
    * Se revisaron visualmente las nubes de palabras generadas para asegurar que las palabras más frecuentes fueran representadas correctamente.
    * Se verificó que solo se incluyeran palabras de más de 5 letras.
    * Se verifico que las imagenes se guardaran en la carpeta "resultados/nubes_palabras"
2.  **Verificación del Procesamiento de Texto:**
    * Se revisó el código para asegurar que el texto se extrajera correctamente de las etiquetas `<p>`.
    * Se verificó que el script manejara correctamente archivos XML con diferentes estructuras.
3.  **Manejo de Errores:**
    * Se probó el script con archivos XML corruptos o inexistentes para verificar que el manejo de errores fuera adecuado (impresión de mensajes de error).

## 4. extractorLinks.py

### Propósito
Este script extrae enlaces (URLs) de los archivos XML generados por `lectorDPF.py`.

### Validación
1.  **Verificación de la Extracción de Enlaces:**
    * Se revisaron manualmente algunos archivos XML para identificar enlaces y se compararon con los resultados del script.
    * Se verificó que el script extrajera enlaces de diferentes partes del XML (texto, atributos, tail).
    * Se verifico que los archivos de texto con los links se guardaran en la carpeta "resultados/links_articulos"
2.  **Verificación de la Expresión Regular:**
    * Se probó la expresión regular con diferentes tipos de URLs para asegurar que funcionara correctamente.
    * Se verificó que el script eliminara enlaces duplicados.
3.  **Manejo de Errores:**
    * Se probó el script con archivos XML corruptos o inexistentes para verificar que el manejo de errores fuera adecuado (impresión de mensajes de error).
    * Se verifico que solo se generaran archivos de texto si se encontraban links.
