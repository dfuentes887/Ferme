from django.urls import path
from .views import UserCreateView

app_name = 'user'

urlpatterns = [
    path('registro-usuario', UserCreateView.as_view(), name= "registro-usuario"),
   
]
