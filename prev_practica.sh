#!/bin/bash

# Definir la ruta base
BASE_DIR="$HOME/Escritorio/ciencia_abierta"

# Definir la carpeta principal dentro de BASE_DIR
RESULTS_DIR="$BASE_DIR/resultados"

# Definir las subcarpetas dentro de "resultados"
SUBFOLDERS=("figuras" "links_articulos" "nubes_palabras" "XML_articulos")

# Crear la carpeta principal si no existe
mkdir -p "$RESULTS_DIR"

# Crear las subcarpetas dentro de "resultados"
for folder in "${SUBFOLDERS[@]}"; do
    mkdir -p "$RESULTS_DIR/$folder"
done

echo "Estructura de carpetas creada en: $RESULTS_DIR"
