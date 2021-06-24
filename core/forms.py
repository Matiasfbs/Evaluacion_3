from django import forms
from django.forms import ModelForm
from .models import Hardware
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserForm(UserCreationForm):

    username=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre de usuario")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.EmailInput(attrs={'class':'form-control'}),label="Correo electronico")
    password1 = forms.CharField(label="Contraseña",help_text='Clave mayor a 10 digitos alfanumerica.',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", help_text="Ingresa la misma contraseña de arriba, para verificar.",widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)


class HardwareForm(ModelForm):

    class Meta:
        model = Hardware
        fields = ['tipoHardware','nombreHardware','precio','anio_lanzamiento','descripcion',]

