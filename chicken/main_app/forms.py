from django import forms
from .models import Eggs

class EggsForm(forms.ModelForm):
    class Meta:
        model = Eggs
        fields = ['color', 'size']