from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'imagen', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el titulo de la noticia'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder': 'Ingrese la descripcion de la noticia'}),
            #'imagen' : forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'})),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }