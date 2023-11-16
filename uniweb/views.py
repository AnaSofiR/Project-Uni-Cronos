from django.shortcuts import render, redirect
from django.http import HttpResponse
import openai
import os
import ast
from .filtrarDatos import *
from .forms import SugerenciaForm
from dotenv import load_dotenv, find_dotenv

# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')


def principal(request):
  #return HttpResponse('<h1>Welcome to home page</h1>')
  if request.method == 'POST':
    horas = request.POST.get('horarios_json')
    materias1 = request.POST.get('materias_json')
    filtrar([materias1])
    profesoresN = request.POST.get('profesores1_json')
    profesoresS = request.POST.get('profesores2_json')
    result = prompt(horas, profesoresS, profesoresN)

    return redirect('horario', result=result)

    
  return render(request, 'principal.html')


def prompt(h, pS, pN):

  ruta_materias_json = os.path.join(os.path.dirname(__file__), 'materias_filtradas.json')

  with open(ruta_materias_json, "r", encoding="utf-8") as file:
    lista_materias = json.load(file)

  horas = h
  profesoresN = pN
  profesoresS = pS  

  #load_dotenv()
  #_ = load_dotenv('openAI.env')
  #print(os.environ)
  openai.api_key  = "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"

  completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[
            {
                "role": "system", "content": "Eres una maquina creadora de horarios universitarios, que se basa en las materias de la universidad y las preferencias del usuario. Estas preferencias seran las horas y dias donde el usuario no podrá ver clase debido a otras responsabilidades, los profesores que prefiere evitar y los profesores que le gustan. El usuario puede no tener horarios no disponibles, así como no tener profdesores que no le gusten y profesores que le gusten. Las materias vendrán con su respectivo horario y profesor. De las materias debes escoger una por materia, respetando las preferencias del usuario. Respondes con un horario posible. Siempre debes tener en cuenta las preferencias del usuario. Tu formato como maquina es el siguiente: x1|h1|p1,x2|h2|p2,...,xn|hn|pn, donde x son las materias, h su horario y p su profesor, en cada horario solo debe haber una materia por nombre respetando las solicitudes del usuario, y solo debes generar un solo formato. En caso de que no encuentres horario, x sería igual a Lo sentimos, h igual a No pudimos encontrar horarios, y p igual a Se puede deber a las preferencias que elegiste. Debes seguir ese formato al pie de la letra, reemplazando cada simbolo segun lo que analices."
            },
            {
                "role": "user", "content": f"Genera un analisis con el siguiente formato. Tu formato como maquina es el siguiente: x1|h1|p1,x2|h2|p2,...,xn|hn|pn. Donde x son las materias, h su horario y p su profesor, hazlo tal cual te muestro en el formato. En cada horario solo debe haber una materia por nombre respetando las solicitudes del usuario, y solo debes generar un solo formato. En caso de que no encuentres horario debido a las preferencias del usuario, dame como resultado el siguiente mensaje con el siguiente formato: Lo sentimos|No pudimos crear un horario|Esto se puede deber a las preferencias que seleccionaste. Debes seguir ese formato al pie de la letra, reemplazando cada simbolo segun lo que analices. Las materias con su respectivo horario y profesor son: {lista_materias} elige una por cada nombre de materia, los horarios no disponibles del usuario son: {horas}, los profesores que el usuario quiere evitar son: {profesoresN} no puedes generar horarios con materias que tengan a este/estos profesores, y los profesores que al usuario le gustan son: {profesoresS}, prioriza las materias que tengan a este profesor. Entrégame la respuesta solo en el formato que te di"
            }
        ]
    )
  
  result1 = completion.choices[0].message["content"]
  result = result1.split(",")
  print(result)

  return result
  

def horario(request, result):

  result_list = ast.literal_eval(result)


  result_data=[]
  for item in result_list:
    materia, horario, profesor = item.split("|")
    result_data.append({'materia': materia, 'horario': horario, 'profesor': profesor})   

  return render(request, 'horario.html', {'horario1_data':result_data})




def buscar(request, lista):
  if request.method == 'POST':
    materia = request.POST.get('searchInput')
    filtrar([materia])

  ruta_materias_json = os.path.join(os.path.dirname(__file__), 'materias_filtradas.json')  

  with open(ruta_materias_json, "r", encoding="utf-8") as file:
    lista_clases = json.load(file)  
 
  return render(request, 'buscar.html', {'lista': lista_clases})

def sugerencias(request):
    if request.method == 'POST':
        form = SugerenciaForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('principal')
    else:
        form = SugerenciaForm()

    return render(request, 'sugerencias.html', {'form': form})  

