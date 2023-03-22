from django import forms
from .models import Grave

class GraveForm(forms.ModelForm):
    class Meta:
        model = Grave
        fields = ['Occupant', 'Birth', 'Death', 'Veteran', "Headstone", "Grid", "Ward", "Block", "Lot"]