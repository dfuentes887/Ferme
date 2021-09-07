from django.contrib.auth.decorators import permission_required
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import User
from .forms import userForm
from django.urls import reverse_lazy



class UserCreateView (CreateView):
     model = User
     form_class = userForm
     template_name = 'crearUser.html'
     success_url = reverse_lazy('core:Index')
     permission_required = 'user.add_user'
     url_redirect  = success_url


     def dispatch(self, request, *args, **kwargs):
         return super().dispatch(request, *args, **kwargs)
     def post(self, request, *args, **kwargs):
         data ={}
         try:
             action = request.POST['action']
             if action == 'add':
                 form = self.get_form()
                 data = form.save()
             else:
                 data['error'] = 'No ha ingresado ninguna opción'
         except Exception as e:
             data['error']  = str(e)
         return JsonResponse(data)


     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['title'] = 'Creación de User'
         context['entity'] = 'Users'
         context['list_url'] = self.success_url
         context['action'] = 'add'
         return context


                