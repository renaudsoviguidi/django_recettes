# forms.py
import json
from django import forms
from .models import Recette


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ("nom_agent", "nom_plat", "url_video", "ingredients", "etapes_preparation", "time")