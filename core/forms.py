from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms.widgets import SelectMultiple
from core.user.models import User 
from core.models import Producto, Csv, Proveedor
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            
            'first_name': forms.TextInput(
                attrs={
                    'placeholder' :'Nombres',
                    'required': 'true'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder' :'Apellidos',
                    'required': 'true'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder' :'Nombre de usuario',
                    'required': 'true'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'placeholder' :'123456789-3',
                    'required': 'true'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder' :'Correo electrónico'
                    
                }
            ),
            
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder' :'Contraseña'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder' :'Confirmar contraseña'
                }
            )
        }
        labels = {'username':'Nombre de usuario','first_name':'Nombres','last_name':'Apellidos','rut':'RUT','email':'Correo Electrónico','password1':'Contraseña','password2':'Repetir Contraseña', 'rango':'RANGO', 'groups': 'UWu' }
        exclude = ['user_permissions', 'last_login','date_joined','is_superuser', 'is_active'  , 'is_staff', 'rango', 'password','groups']


class CustomUserCreationForm2(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            
            'first_name': forms.TextInput(
                attrs={
                    'placeholder' :'Nombres',
                    'required': 'true'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder' :'Apellidos',
                    'required': 'true'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder' :'Nombre de usuario',
                    'required': 'true'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'placeholder' :'123456789-3',
                    'required': 'true'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder' :'Correo electrónico'
                    
                }
            ),
            
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder' :'Contraseña',
                    'required' : 'false'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder' :'Confirmar contraseña',
                    'required' : 'false'
                }
            )
        }
        labels = {'username':'Nombre de usuario','first_name':'Nombres','last_name':'Apellidos','rut':'RUT','email':'Correo Electrónico','password1':'Contraseña','password2':'Repetir Contraseña', 'rango':'RANGO', 'groups': 'UWu' }
        exclude = ['user_permissions', 'last_login','date_joined','is_superuser', 'is_active'  , 'is_staff', 'rango', 'password','groups', 'password1','password2']

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'    
        labels = {'stockCritico':'Stock Crítico', 'tipoFamilia': 'Tipo de familia', 'tipo': 'Familia del producto'}
        widgets = {
            
            'fechaVenc': forms.DateInput(
                attrs={
                    'placeholder' :'DD/MM/AAAA'
                }
            )
            
        }

FORMA_PAGO= (
    ('Tarjeta', 'Tarjeta de crédito'),
    ('Webpay', 'WebPay')
    
)

class CheckoutForm(forms.Form):
    direccion = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' :'Av.Chile #123',
        'class' : 'form-control'
    }))
    apartamento =  forms.CharField(required=False , widget=forms.TextInput(attrs={
        'placeholder' :'Apartamento (opcional)',
        'class': 'form-control'
    }))
    pais = CountryField(blank_label='(Seleccionar país)').formfield(widget= CountrySelectWidget(
        attrs={
            'class': 'custom-select d-block w-100'
        }
    ))
    zip = forms.CharField(max_length=10 ,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Código Postal'
    }))
    misma_direccion =  forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'label': 'gei'
        
    }) )
    guardar_info =  forms.BooleanField( required=False,widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
        
    }) )
    opcion_de_pago = forms.ChoiceField(widget=forms.RadioSelect,choices= FORMA_PAGO)
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder' :'+56971235125',
        'class': 'form-control'
    }))

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('archivo',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            
            'name': forms.TextInput(
                attrs={
                    'placeholder' :'Nombre del grupo',
                    'required': 'true',
                    
                }
            
            ),
             'permissions': forms.SelectMultiple(
                attrs={
                    'placeholder' :'Permisos',
                    'style' : 'height:300px'
                    
                    
                }
            
            ),
            
        }
        labels = {'name':'Nombre del grupo' ,'permissions': 'Permisos del grupo' }
        
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        placeholder = {'nombre': 'Nombre del proovedor', 'telefono' : 'Teléfono del proveedor', 'rubro': 'Rubro del proveedor', 'codigo':'Ejemplo: 999','categoria': 'Categoría' }
        labels = {'nombre': 'Nombre', 'telefono' : 'Teléfono ', 'rubro': 'Rubro', 'codigo':'Código','categoria': 'Categoría' }
        
      