from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'type', 'price']
        widgets = {
            'type': forms.Select(choices=Flight.Type_Choices),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError('El nombre es obligatorio.')
        return name
