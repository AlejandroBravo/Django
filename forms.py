from django import forms

class RegForm(forms.Form):
	nombre = forms.charfield(max_length=100)
	edad = forms.interferfield()