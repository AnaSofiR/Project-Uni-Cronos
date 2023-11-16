import os
import openai
import json
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv('openAI.env')
openai.api_key  = os.environ['openAI_api_key']

with open('materias_filtradas.json', 'r') as file:
    file_content = file.read()
    materiasDisponibles = json.loads(file_content)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

instruction = "Eres un recomendador de horarios universitarios, los horarios abarcarán los dias lunes \
a viernes, deben ser precisos y las clases no deben chocar con otras en los horarios establecidos. \
También se tendrá en cuenta profesores y horarios que a los usuarios no les gusten o no puedan \
estar por actividades extracurriculares respectivamente"


def creacionHorario(horarios, profesoresN, profesoresS):
    prompt = f"{instruction} Has una recomendación de horario en base a las materias disponibles en el json, \
    elige una sola opción de cada materia, descarta las materias que sean en los mismos horarios que el\
    usuario no puede ver clase y descarta las materias que tengan los profesores \
    que al usuario no le gustan, pero prioriza las materias con los profesores que sí le\
    gustan {materiasDisponibles, horarios, profesoresN, profesoresS}"

    print(prompt)

    response = get_completion(prompt)

    print(response)
    return response
