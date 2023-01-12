from django.utils.translation import gettext_lazy as _
from django import forms
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'modalidade']
