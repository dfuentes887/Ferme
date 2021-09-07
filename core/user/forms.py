
from django.forms import *
from django.http import request
from .models import User
from django.contrib.auth.forms import UserCreationForm

class userForm (UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'rut', 'email', 'password1', 'password2'
        widgets = {
            
            'first_name': TextInput(
                attrs={
                    'placeholder' :'Nombres',
                    'required': 'True'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder' :'Apellidos'
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder' :'Nombre de usuario'
                }
            ),
            'rut': TextInput(
                attrs={
                    'placeholder' :'123456789-3'
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder' :'Correo electrónico'
                }
            ),
            
            'password1': PasswordInput(
                attrs={
                    'placeholder' :'Contraseña'
                }
            ),
            'password2': TextInput(
                attrs={
                    'placeholder' :'Confirmar contraseña'
                }
            )
        }
        exclude = ['groups' , 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active' , 'is_staff']
        labels = {'username':'Nombre de usuario','first_name':'Nombres','last_name':'Apellidos','rut':'RUT','email':'Correo Electrónico','password1':'Contraseña','password2':'Repetir Contraseña', 'rango':'RANGO', 'groups': 'UWu' }
    def save(self, commit = True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password1', 'password2']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk = u.pk)
                    if user.password1 != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data 

        
       
        
           
    
    
