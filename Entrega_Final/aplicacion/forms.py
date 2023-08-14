from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class Ofi_Form(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    direccion = forms.CharField(label="Direccion", max_length=50, required=True)

class Eve_Form(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    tipo = forms.CharField(label="Direccion", max_length=50, required=True)
   

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Nombre", max_length=50, required=False)
    last_name= forms.CharField(label="Apellido", max_length=50, required=False)

    class Meta:
        model=User
        fields= ['email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts= { k:"" for k in fields}
class AvatarFormulario(forms.Form):
    imagen=forms.ImageField(required=True)