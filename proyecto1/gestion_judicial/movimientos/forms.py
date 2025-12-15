from django import forms
from .models import Movimiento

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['fecha', 'descripcion', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
