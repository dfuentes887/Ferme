from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

ELEGIR_RANGO = (
    ('ADM','Administrador'),
    ('VEN','Vendedor'),
    ('EMP','Empleado'),
    ('CLI','Cliente'),
    ('PRO','Proveedor')


           
)


class User(AbstractUser):
    rut = models.CharField(max_length=15)
    now = timezone.now()
    rango = models.CharField(choices= ELEGIR_RANGO, max_length= 3 , default= "CLI")
    
    

  


    
  


