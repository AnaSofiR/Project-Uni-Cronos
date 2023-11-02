from django.db import models

# Create your models here.
class profesor(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=2)

class dia(models.Model):
    nombre = models.CharField(max_length=10)

class hora(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class clase_taller(models.Model):
    horario = models.ManyToManyField(dia, through='horarioTaller')
    profesor = models.ForeignKey(profesor, on_delete=models.CASCADE)    

class materia(models.Model):
    nombre = models.CharField(max_length=20)
    profesor = models.ForeignKey(profesor, on_delete=models.CASCADE)
    horario = models.ManyToManyField(dia, through='horarioMateria')
    horario_taller = models.ForeignKey(clase_taller, on_delete=models.CASCADE)        

class horarioMateria(models.Model):
    materia = models.ForeignKey(materia, on_delete=models.CASCADE)
    dia = models.ForeignKey(dia, on_delete=models.CASCADE)
    hora = models.ForeignKey(hora, on_delete=models.CASCADE)

class horarioTaller(models.Model):
    clase_taller = models.ForeignKey(clase_taller, on_delete=models.CASCADE) 
    dia = models.ForeignKey(dia, on_delete=models.CASCADE)
    hora = models.ForeignKey(hora, on_delete=models.CASCADE)


class MateriaSeleccionada(models.Model):
    nombre = models.CharField(max_length=100)
