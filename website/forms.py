from django import forms
from .models import Grave

class GraveForm(forms.ModelForm):
    class Meta:
        model = Grave
        fields = ['first_name', 'last_name', 'middle_name', 'birth', 'death', 'veteran', "headstone", "reference", "Grid", "Ward", "Block", "Lot","Plot"]