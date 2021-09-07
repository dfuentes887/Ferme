#ESTO ES PA LA TARJETA
from os import name
from django.contrib.auth.models import User
from django.core import paginator
from django.http.response import Http404, HttpResponseRedirect
import stripe 
from django.conf import settings
from django.contrib.auth import get_user_model


#ESTO ES PA BUSCAR
from django.db.models import Q
from django.core.paginator import Paginator


from django.shortcuts import render,redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView ,View
from django.utils import timezone

#PARA LOS FORMS
from .forms import CheckoutForm
from .forms import CsvModelForm
from .forms import CustomUserCreationForm,CustomUserCreationForm2, ProductoForm , GroupForm, ProveedorForm

#ESTO ES PARA EL PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .utils import render_to_pdf
#Traer del models algunos modelos
from core.models import Producto, OrderProducto ,Order , DireccionFactura, Pago , Csv , Marca, Proveedor, TipoFamilia, TipoProducto
from core.user.models import User
from django.contrib.auth.models import Group , Permission
import csv
stripe.api_key = settings.STRIPE_SECRET_KEY


#PDF NUEVO
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



# Create your views here.
def Index (request):
    return render(request,'app/Index.html')

def Prueba(request):
    return render(request, 'app/prueba.html')

def registro(self):
    data = {
        'form': CustomUserCreationForm()
    }
    if self.method == 'POST':
        
        formulario = CustomUserCreationForm(data=self.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login (self, user)
            
            
            messages.success(self, "Te has registrado correctamente.")
            return redirect(to= "core:Index")
        else:
            messages.success(self, "Contraseña / Usuario incorrectos .")
        data["form"] = formulario

    return render(self, 'registration/registro.html', data)

def logout (request):
    return render(request,'registration/logout.html')



def agregar_producto(request):
    tipo = TipoFamilia.objects.all()
    proveedores = Proveedor.objects.all()
    page = request.GET.get('page', 1)
    buscador = request.GET.get("buscador")
    try:
        paginator = Paginator(tipo, 4)
        tipo = paginator.page(page)
    except:
        raise Http404


    if buscador:
        tipo = TipoFamilia.objects.filter(
            Q(nombre__icontains = buscador)
        ).distinct
    mydict = {
        'form': ProductoForm(),
        'entity': tipo,
        'proveedores': proveedores,
        'paginator' : paginator
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        

        if formulario.is_valid():
    
                
               

            formulario.save()
            messages.success(request, "Producto guardado correctamente.")
            return redirect(to= "core:listar-productos")
        else:
            mydict["form"] = formulario
    
    return render(request,'app/productos/agregar.html',context=mydict)

def menu_productos(request):
    return render(request, 'app/productos/menu.html')

def listar_productos(request):
    page = request.GET.get('page', 1)
    productos = Producto.objects.all()
    try:
        paginator = Paginator(productos, 8)
        productos = paginator.page(page)
    except:
        raise Http404
    
    
    mydict={
        'entity': productos,
        'paginator' : paginator
    }
    return render(request, 'app/productos/listar.html', context=mydict)

def modificar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    tipo = TipoFamilia.objects.all().order_by('-tipo')
    proveedores = Proveedor.objects.all()
    mydict = {
        'form': ProductoForm(instance=producto),
        'tipo':tipo,
        'proveedores':proveedores
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente.")
            return redirect(to= "core:listar-productos")
            

    return render(request, 'app/productos/modificar.html',context=mydict)

def modificar_user(request,id):
    users = get_object_or_404(User, id=id)

    data = {
        'form': CustomUserCreationForm2(instance=users)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm2(data = request.POST, instance=users, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario modificado correctamente.")
            return redirect(to= "core:listado-personas")
            

    return render(request, 'registration/modificarUsers.html', data)

def eliminar_productos(request ,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente.")
    return redirect(to= "core:listar-productos")

def eliminar_usuario(request ,id):
    users = get_object_or_404(User, id=id)
    users.delete()
    messages.success(request, "Usuario eliminado correctamente.")
    return redirect(to= "core:listado-personas")




#--------------------------------------------------TIENDA--------------------------------------
def listado_productos(request):
    
    
    productos = Producto.objects.all()
    buscador = request.GET.get("buscador")
    categoria = request.GET.get("categoria")
   
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 8)
        productos = paginator.page(page)
    except:
        raise Http404

    if buscador:
        productos = Producto.objects.filter(
            Q(nombre__icontains = buscador)
        ).distinct

    if categoria:
        productos = Producto.objects.filter(
            Q(categoria__icontains = categoria) 
        ).distinct()
    
    return render(request, 'app/vista_cliente/listaproductos.html', {'entity': productos , 'paginator' : paginator} )


class ProductView(ListView):
    
    model = Producto
    paginate_by= 12
    template_name = "app/vista_cliente/listado_productos.html"
    


class ProductoVer(DetailView):
    model = Producto
    template_name = "app/vista_cliente/producto.html"
@login_required
def add_to_cart (request,slug):
   
    producto = get_object_or_404(Producto, slug = slug)
    order_producto ,created = OrderProducto.objects.get_or_create(
        producto = producto,
        user=request.user,
        
    )
    order_qs = Order.objects.filter(user=request.user , ordered=False)
    if order_qs.exists():
        order = order_qs [0]
        if order.productos.filter(producto__slug = producto.slug).exists():
            order_producto.cantidad += 1
            
            order_producto.save()
        else:
            order.productos.add(order_producto)
            
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user= request.user, ordered_date = ordered_date)
        order.productos.add(order_producto) 
    
    messages.success(request, "El producto fue agregado al carrito de compras.")
    return redirect("core:producto" ,slug = slug)    

def add_single_to_cart (request,slug):

    producto = get_object_or_404(Producto, slug = slug)
    order_producto ,created = OrderProducto.objects.get_or_create(
        producto = producto,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user , ordered=False)
    if order_qs.exists():
        order = order_qs [0]
        if order.productos.filter(producto__slug = producto.slug).exists():
            order_producto.cantidad += 1
            order_producto.save()
        else:
            order.productos.add(order_producto)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user= request.user, ordered_date = ordered_date)
        order.productos.add(order_producto) 
    messages.success(request, "El carrito fue actualizado.")
    return redirect("core:carrito")    

def remove_from_cart (request,slug):
    producto = get_object_or_404(Producto,slug = slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs [0]
        if order.productos.filter(producto__slug = producto.slug).exists():
            order_producto = OrderProducto.objects.filter(
        producto = producto,
        user=request.user
    )[0]
            order.productos.remove(order_producto)
        else:
            return redirect("core:producto" ,slug = slug)   
    else:
        return redirect("core:producto" ,slug = slug)   
    return redirect("core:producto" ,slug = slug)    
    

class CheckoutView (View):
    def get(self, *args ,**kwargs):
        #Formulario
       
        form = CheckoutForm()
        mydict = {
            'form' : form
        }
        return render(self.request, "app/vista_cliente/checkout.html" , context=mydict)
        
    def post(self, *args, **kwargs):
        form  = CheckoutForm(self.request.POST or None)
        try:
            order  = Order.objects.get(user=self.request.user , ordered= False)
            if form.is_valid():
                direccion  = form.cleaned_data.get('direccion')
                apartamento = form.cleaned_data.get('apartamento')
                pais = form.cleaned_data.get('pais')
                zip = form.cleaned_data.get('zip')
                misma_direccion = form.cleaned_data.get('misma_direccion')
                #guardar_info = form.cleaned_data.get('guardar_info')
                opcion_de_pago = form.cleaned_data.get('opcion_de_pago')
                telefono = form.cleaned_data.get('telefono')
                direccion_factura= DireccionFactura(
                    user = self.request.user,
                    direccion = direccion,
                    apartamento  =apartamento ,
                    pais = pais,
                    zip = zip,
                    #TODO: Añadir Funcionalidad pa estos campos
                    #misma_direccion = misma_direccion,
                    #guardar_info = guardar_info,
                    opcion_de_pago = opcion_de_pago,
                    telefono = telefono
            )
                direccion_factura.save()
                order.direccion_factura = direccion_factura
                order.save()

                if opcion_de_pago =='Tarjeta':
                    return redirect('core:finalizar-compra')
                elif opcion_de_pago == 'Webpay':
                    return redirect('core:finalizar-compra')
                    #return redirect('core:pago', opcion_de_pago = 'WebPay')
                else:
                    messages.warning(self.request, "Opción inválida, seleccione otro método de pago")
                    return redirect('core:checkout')
                messages.error(self.request , "El checkout ha sido completao")
                return redirect ('core:checkout')
            messages.error(self.request , "El checkout ha fallado")
            return redirect ('core:checkout')
        except ObjectDoesNotExist:
           
            return redirect("core:carrito")

            



       
        

class carrito(LoginRequiredMixin, View):
    def get(self , *args ,**kwargs):
        try:
            order  = Order.objects.get(user=self.request.user , ordered= False)
            data = {
                'object' : order
            }
            return render(self.request, 'app/vista_cliente/carrito.html', data)
        except ObjectDoesNotExist:
            messages.error(request, "No tienes ninguna orden activa todavía")
            return redirect("/")
       
def remove_single_from_cart(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.productos.filter(producto__slug=producto.slug).exists():
            order_producto = OrderProducto.objects.filter(
                producto=producto,
                user=request.user
            )[0]
            if order_producto.cantidad > 1:
                order_producto.cantidad -= 1
                order_producto.save()
            else:
                order.productos.remove(order_producto)
            messages.info(request, "El carrito fue actualizado.")
            return redirect("core:carrito")
        else:
            messages.info(request, "Este producto no está en tu carrito.")
            return redirect("core:producto", slug=slug)
    else:
        messages.info(request, "No tienes una orden activa aún.")
        return redirect("core:producto", slug=slug)

class OrdenPDF(View):
    
    def get(self ,request, *args ,**kwargs):
            order  = Order.objects.get(user=self.request.user , ordered= False)
            data = {
                'object' : order
            }
            
            pdf = render_to_pdf('app/vista_cliente/pdf.html',data)
            pdf['Content-Disposition'] = 'attachment; filename = "report.pdf"'
            return HttpResponse(pdf, content_type = 'application/pdf')

class DownloadPDF(View):
    def get(self,request,*args, **kwargs):
        order  = get_object_or_404(Order,user=self.request.user , ordered= False)
        data = {
            'object' : order
        }
        try:
            pdf = render_to_pdf('app/vista_cliente/pdf.html',data)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Boleta%s.pdf" %(" Electrónica")
            content = "attachment; filename= %s" %(filename)
            response['Content-Disposition'] = content
            order.ordered = True
            order.save()
            
            return response
        except Order.DoesNotExist:
            return redirect ("core:Index")
            
            
    
        
        
        
        
        
        
    

        
        

def finalizar_pago (request):
    return render(request,'app/vista_cliente/finalizar_compra.html')

def carro (request):
    return render(request,'app/vista_cliente/carro.html')





def pago_realizado (request):
    return render(request,'app/vista_cliente/pago_realizado.html')      
                
            


class VistaPago(View):
    def get (self, *args, **kwargs):
        return render(self.request, "app/vista_cliente/pago.html")
    
    def post (self, *args, **kwargs):
        
        order = Order.objects.get(user = self.request.user , ordered = False)
        token = self.request.POST.get('stripeToken')
        amount =int(order.get_total() * 100)
        try:
            charge = stripe.Charge.create(
                amount = amount,
                currency= "usd",
                source = token
        )
                
            #CREAR EL PAGO
            pago = Pago ()
            pago.stripe_charge_id = charge["id"]
            pago.user = self.request.user
            pago.amount = int(order.get_total())
            pago.save()

            #Unir el pago a la orden 
            order.ordered = True
            order.pago = pago
            order.save()

            messages.success(self.request, "Tu orden ha sido exitosa")
            return redirect("/")

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.error (self.request, f"{err.get('message')}")
            return redirect("/")
        except stripe.error.RateLimitError as e:
            messages.error (self.request, "Limite de Rate")
            return redirect("/")
        # Too many requests made to the API too quickly
            
           
        except stripe.error.InvalidRequestError as e:
            messages.error (self.request, "Éxito")
            order.ordered = True
          
            order.save()
                
            return redirect("/")
        # Invalid parameters were supplied to Stripe's API
            
        except stripe.error.AuthenticationError as e:
            messages.error (self.request, "Error de autenticación")
            return redirect("/")
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
           
        except stripe.error.APIConnectionError as e:
            messages.error (self.request, "Error de conexión ")
            return redirect("/")
        # Network communication with Stripe failed
            
        except stripe.error.StripeError as e:
            messages.error (self.request, "Error de Stripe, algo ha salido mal. Por favor intenta de nuevo.")
            return redirect("/")
        # Display a very generic error to the user, and maybe send
        # yourself an email
            
        except Exception as e:
            messages.error (self.request, "Se ha producto un error")
            return redirect("/")
        # Something else happened, completely unrelated to Stripe
            

def upload_file_view (request): 
    form = CsvModelForm(request.POST or  None , request.FILES or None)
    if form.is_valid():
        form.save()
        
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open (obj.archivo.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader) :
                if i == 0:
                    pass
            
                else:
                    row = "".join(row)
                    row = row.replace (";"," ")
                    row = row.split()
                    nombre = row[0].capitalize()
                    
                    Marca.objects.create(
                        nombre = nombre,
                        codigo = int(row[1])

                    )
                    #print(row)
                    #print(type(row))
                obj.activated = True
                obj.save()
        messages.success(request, "Las marcas se han registrado.")
        return redirect ("core:listar-productos")
    return render(request, 'app/productos/subir_archivo.html', {'form':form})
       

       
def listado_personas(request):
    users = User.objects.all() 
    return render(request, 'registration/listadoUsers.html', {'users': users} )   


class SaleInvoicePdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template ( 'app/productos/boleta.html')
            context = {
                'order' : Order.objects.get(user=self.request.user , ordered= False),
                'productos' : Producto.objects.all(),
                'user' : request.user
                
                
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf' )
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
           
            return  response
        except Exception as e:
            pass
        return HttpResponseRedirect(reverse_lazy('core:carrito'))

def finalizarCompra (request):
    return render(request,'app/productos/finalizarCompra.html')
        

def listaGrupos (request):
    group = Group.objects.all()

    return render(request, 'registration/listaGrupos.html', {'group' : group})      


def listaGrupos_add (request):
  
    data = {
        'form' : GroupForm()
    }
    if request.method == 'POST':
        formulario = GroupForm(data = request.POST )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto guardado correctamente.")
            return redirect(to= "core:listado-groups")
        else:
            data['form'] = formulario
    return render(request,'registration/listaGruposAdd.html',data)
def listaGrupos_change(request,id):
    groups = get_object_or_404(Group, id=id)
    data = {
        'form': GroupForm(instance=groups)
    }
    if request.method == 'POST':
        formulario = GroupForm(data=request.POST, instance=groups)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Grupo modificado correctamente.")
            return redirect(to= "core:listado-groups")
    return render(request, 'registration/listaGruposChange.html', data)

def listaGrupos_del (request,id):
    group = get_object_or_404(Group, id=id)
    group.delete()
    messages.success(request, "Grupo eliminado correctamente.")
    return redirect(to= "core:listado-groups")


def userGroup(request,id):
    users = User.objects.get(id = id)
    
    ugroup = []
    for i in users.groups.all():
        print(i.name)
        
        ugroup.append(i)
    group = Group.objects.all()
    mydict = {'ugroup':ugroup, 'group':group , 'id' :id}

    return render(request, 'registration/userGroup.html', context=mydict )

def userGroup_add(request,id):
    if request.method == 'POST':
        gname = request.POST.get('gname')
        group =Group.objects.get(name=gname)
        user = User.objects.get(id=id)
        user.groups.add(group)
        
        messages.success(request, "Grupo agregado al usuario.")
    return redirect('core:userGroup', id=id)



def userGroup_delete(request,id ,name):
    
    group =Group.objects.get(name=name)
    user = User.objects.get(id=id)
    user.groups.remove(group)
        
    messages.success(request, "Grupo en el usuario eliminado.")
    return redirect('core:userGroup', id=id)
    
def listar_proveedores(request):
    
    proveedores = Proveedor.objects.all()
    
    data={
        'proveedores': proveedores
    }
    return render(request, 'app/productos/proveedor/lista.html', data)

def agregar_proveedores(request):
    mydict = {
        'form': ProveedorForm(),
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor guardado correctamente.")
            return redirect(to= "core:listar_proveedores")
        else:
            mydict["form"] = formulario
    
    return render(request,'app/productos/proveedor/agregar.html',context=mydict)

def modificar_proveedores(request,id):
    proveedores = get_object_or_404(Proveedor, id=id)
    
    mydict = {
        'form': ProveedorForm(instance=proveedores),
        
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data = request.POST, instance=proveedores, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor modificado correctamente.")
            return redirect(to= "core:listar_proveedores")
            

    return render(request, 'app/productos/proveedor/modificar.html',context=mydict)

def eliminar_proveedores(request ,id):
    proveedores = get_object_or_404(Proveedor, id=id)
    proveedores.delete()
    messages.success(request, "Proveedor eliminado correctamente.")
    return redirect(to= "core:listar_proveedores")


def manual_de_usuario (request):

    return render(request, 'app/vista_cliente/manual.html')