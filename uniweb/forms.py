# forms.py

from django import forms
from .models import Sugerencia

class SugerenciaForm(forms.ModelForm):
    class Meta:
        model = Sugerencia
        fields = ['nombre', 'sugerencia']
