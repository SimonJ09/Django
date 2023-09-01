from django import forms
from .models import MonModel

class InfoForm(forms.ModelForm):
    class Meta:
        model = MonModel
        fields = '__all__'
