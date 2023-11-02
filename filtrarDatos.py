import pandas as pd
import json

with open("materias.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.json_normalize(data, 'horarios_clases')

materias_a_filtrar = ["Cálculo 1", "Lógica", "Álgebra Lineal"]

resultados_filtrados = []

for materia in materias_a_filtrar:
    materia_filtrada = df[df['materia'] == materia]
    resultados_filtrados.extend(materia_filtrada.to_dict(orient='records'))

nombre_archivo = "materias_filtradas.json"

with open(nombre_archivo, 'w', encoding='utf-8') as json_file:
    json.dump(resultados_filtrados, json_file, ensure_ascii=False, indent=4)