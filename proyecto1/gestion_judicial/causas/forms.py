from django import forms
from .models import Causa

class CausaForm(forms.ModelForm):
    class Meta:
        model = Causa
        fields = [
            'competencia',
            'corte',
            'tribunal',
            'tipo_causa',
            'rol',
            'anio',
            'descripcion',
            'estado',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
