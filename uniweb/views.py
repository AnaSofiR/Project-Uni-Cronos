from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def principal(request):
  #return HttpResponse('<h1>Welcome to home page</h1>')
    
  return render(request, 'principal.html')

def procesar_formulario(request):
    if request.method == 'POST':
        profesoresS = request.POST.get('profesores1_json')
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            dato = formulario.cleaned_data['dato']
            # Realiza alguna acción con los datos, por ejemplo, imprimirlos
            print(dato)
            # Puedes realizar alguna acción adicional con los datos aquí
            return render(request, 'exito.html')
    else:
        formulario = MiFormulario()
    return render(request, 'formulario.html', {'formulario': formulario})
