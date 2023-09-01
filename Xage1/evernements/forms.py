from django import forms
from .models import Evenement

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['nom', 'description', 'pdf', 'photo', 'date_debut', 'date_fin']
