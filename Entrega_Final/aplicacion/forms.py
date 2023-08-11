from django import forms
class Sus_Form(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)

class Ser_Form(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    encargado = forms.CharField(label="Encargado", max_length=50, required=True)

class Cli_Form(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    servicio_contratado = forms.CharField(label="Servicio Contratado", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)