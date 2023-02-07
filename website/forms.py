from django import forms
from .models import Grave

class GraveForm(forms.ModelForm):
    class Meta:
        model = Grave
        fields = ['FirstName', 'LastName', 'Birth', 'Death', 'Veteran'] #"Headstone", "Reference", "Grid", "Ward", "Block", "Lot","Plot"]