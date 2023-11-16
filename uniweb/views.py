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
    materias = request.POST.get('materias_json')
    print(materias)
    materias1 = list(materias)
    filtrar(materias1)
    profesoresN = request.POST.get('profesores1_json')
    profesoresS = request.POST.get('profesores2_json')
    h1, h2, h3 = prompt(horas, profesoresS, profesoresN)

    return redirect('horario', horario1=h1, horario2=h2, horario3=h3)

    
  return render(request, 'principal.html')


def prompt(h, pS, pN):

  ruta_materias_json = os.path.join(os.path.dirname(__file__), 'materias_filtradas.json')  

  with open(ruta_materias_json, "r", encoding="utf-8") as file:
    lista_materias = json.load(file)

  horas = h
  profesoresN = pN
  profesoresS = pS  

  
  _ = load_dotenv('openAI.env')
  print(os.environ)
  openai.api_key  = os.environ['openAI_api_key']

  completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[
            {
                "role": "system", "content": "Eres una maquina creadora de horarios universitarios, que se basa en las materias de la universidad y las preferencias del usuario. Estas preferencias seran las horas y diasdonde el usuario no podrá ver clase debido a otras responsabilidades, los profesores que prefiere evitar y los profesores que le gustan. Los horarios no disponibles del usuario, los profesores que prefiere evitar y los profesores que le gusten pueden estar vacíos. Las materias vendrán con su respectivo horario y profesor. De las materias debes escoger una por materia, respetando las preferencias del usuario. Debes generar tres posibles horarios. Respondes primero con el primer horario, cada materia con su respectivo horario y profesor. Luego responde con el segundo horario con el mismo formato que el anterior. Luego respondes con el tercer posible horario con el mismo formato que el anterior. Si en alguno de los casos no existe un horario disponible debido a las preferencias del usuario, deja ese espacio en blanco. Siempre debes tener en cuenta las preferencias del usuario. Tu formato como maquina es el siguiente: x1:h1:p1--x2:h2:p2--...--xn:hn:pn // x1:h1:p1--x2:h2:p2--...--xn:hn:pn // x1:h1:p1--x2:h2:p2--...--xn:hn:pn. Donde x son las materias, h su horario y p su profesor, así en los tres horarios. Debes seguir ese formato al pie de la letra, reemplazando cada simbolo segun lo que analices. Un ejemplo de output por tu parte, teniendo en cuenta que existan 3 posibles horarios sería: Cálculo I|[lunes:10:00am-11:30am,martes:12:00pm-1:30pm]|Dr.Juan Martínez--Álgebra Lineal|[miércoles:12:00pm-1:30pm]|Dr. José García--... // Cálculo I|[jueves:4:00pm-5:30pm,viernes:12:00pm-1:30pm]|Dr. Cecilia Rendón--Álgebra Lineal|[viernes:12:00pm-1:30pm]|Dr. Walter Ramírez--... // Cálculo I|[martes:10:00am-11:30am,jueves:2:00pm-3:30pm]|Dr. Hector Ospina--Álgebra Lineal|[lunes:1:30pm-3:00pm]|Dr. José García--.... En caso de que solo existan dos posibles horarios, tu output sería:  Cálculo I|[lunes:10:00am-11:30am,martes:12:00pm-1:30pm]|Dr.Juan Martínez**Álgebra Lineal|[miércoles:12:00pm-1:30pm]|Dr. José García--... // Cálculo I|[jueves:4:00pm-5:30pm,viernes:12:00pm-1:30pm]|Dr. Cecilia Rendón**Álgebra Lineal|[viernes:12:00pm-1:30pm]|Dr. Walter Ramírez--...//Lo sentimos|No fue posible crear más horarios|Se puede deber a las preferencias que elegiste"
            },
            {
                "role": "user", "content": f"Genera un analisis con el siguiente formato. Tu formato como maquina es el siguiente: x1:h1:p1--x2:h2:p2--...--xn:hn:pn // x1:h1:p1--x2:h2:p2--...--xn:hn:pn // x1:h1:p1--x2:h2:p2--...--xn:hn:pn. Donde x son las materias, h su horario y p su profesor, así en los tres horarios. Debes seguir ese formato al pie de la letra, reemplazando cada simbolo segun lo que analices. Las materias son: {lista_materias}, los horarios no disponibles del usuario son: {horas}, los profesores que el usuario prefiere evitar son: {profesoresN} y los profesores que al usuario le gustan son: {profesoresS}"
            }
        ]
    )
  
  result = completion.choices[0].message["content"]
  
  horario1,horario2,horario3 = result.split(" // ")
  horario1 = horario1.split("**")
  horario2 = horario2.split("**")
  horario3 = horario3.split("**")

  return horario1, horario2, horario3
  

def horario(request, horario1, horario2, horario3):
    
    horario1_list = ast.literal_eval(horario1)
    horario2_list = ast.literal_eval(horario2)
    horario3_list = ast.literal_eval(horario3)


    horario1_data=[]
    horario2_data=[]
    horario3_data=[]
    for item in horario1_list:
      materia, horario, profesor = item.split("|")
      horario1_data.append({'materia': materia, 'horario': horario, 'profesor': profesor})

    for item in horario2_list:
      materia, horario, profesor = item.split("|")
      horario2_data.append({'materia': materia, 'horario': horario, 'profesor': profesor})

    for item in horario3_list:
      materia, horario, profesor = item.split("|")
      horario3_data.append({'materia': materia, 'horario': horario, 'profesor': profesor})    
    
    context = {
        'horario1_data': horario1_data,
        'horario2_data': horario2_data,
        'horario3_data': horario3_data,
    }

    return render(request, 'horario.html', context)




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

