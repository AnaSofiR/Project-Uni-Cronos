import pandas as pd
import json
import os

ruta_materias_json = os.path.join(os.path.dirname(__file__), 'materias.json')

with open(ruta_materias_json, "r", encoding="utf-8") as file:
    data = json.load(file)

def filtrar(materias):
    # Normalizar el JSON usando la clave "horarios_clases"
    df = pd.json_normalize(data, 'horarios_clases')

    # Filtrar las clases según las materias
    clases_filtradas = df[df['materia'].isin(materias)].to_dict(orient='records')

    # Ruta del archivo de salida
    ruta_archivo_salida = os.path.join(os.path.dirname(__file__), 'materias_filtradas.json')
    
    # Guardar las clases filtradas en un nuevo archivo JSON
    with open(ruta_archivo_salida, 'w', encoding='utf-8') as json_file:
        json.dump(clases_filtradas, json_file, ensure_ascii=False, indent=4)

# Ejemplo de uso con una lista de materias

