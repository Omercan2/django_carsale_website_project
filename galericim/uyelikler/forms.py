from django import forms
from .models import Araba

class ArabaForm(forms.ModelForm):
    class Meta:
        model = Araba
        fields = '__all__'