
from django.db import models
from django.conf import settings
from django.db.models.fields import CharField, IntegerField, PositiveIntegerField
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms
# Create your models here.
class Comuna(models.Model):
    nombre= models.CharField(max_length=50) 

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    comuna = models.ForeignKey(Comuna, on_delete= models.PROTECT)


#------------------------------TIENDA------------------------------#
class Marca(models.Model):
    nombre =  models.CharField (max_length=50)
    codigo = PositiveIntegerField()
    
    def __str__(self):
        return self.nombre  

ELEGIR_CATEGORIA = (
    ('Herramientas','Herramienta'),
    ('Indumentarias','Indumentaria'),
    ('Iluminación','Iluminación_Y_Redes'),
    ('Materiales','Material'),
    ('Maderas','Madera') 
)




class TipoProducto(models.Model):
    nombre =  models.CharField (max_length=50)
    SKU = models.CharField (max_length=3 , unique=True)
     
    def __str__(self):
        return '%s %s' % (self.SKU , self.nombre)

class TipoFamilia (models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField (max_length=3 , unique=True)
    tipo = models.ForeignKey(TipoProducto, on_delete =models.PROTECT)
    categoria = models.CharField(choices= ELEGIR_CATEGORIA, max_length= 20)
    def __str__(self):
        return '%s %s' % (self.codigo , self.nombre)

class Proveedor (models.Model):
    nombre  = models.CharField(max_length=25)
    telefono = models.IntegerField()
    rubro = models.CharField( max_length=255  )
    codigo = models.IntegerField()
    categoria = models.CharField(choices= ELEGIR_CATEGORIA, max_length= 20)
    correo = models.EmailField()
    def __str__(self):
        return '%s %s' % (self.codigo , self.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete =models.PROTECT)
    tipo = models.ForeignKey(TipoProducto, on_delete =models.PROTECT)
    tipoFamilia = models.ForeignKey(TipoFamilia, on_delete =models.PROTECT)
    proveedor = models.ForeignKey(Proveedor ,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to = "productos",null= True)
    fechaVenc = models.DateField(blank=True , null = True)
    slug = models.SlugField()
    stock = models.IntegerField()
    stockCritico = models.IntegerField()
    categoria = models.CharField(choices= ELEGIR_CATEGORIA, max_length= 20)

    def __str__(self):
        return self.tipo

    def get_absolute_url(self):
        return reverse("core:producto", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("core:finalizar-pago", kwargs={
            'user': self.user
        })
    



class OrderProducto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE , blank= True , null=True)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    
    def __str__(self):
        return f"{self.cantidad} of {self.producto.nombre}"

    def total_a_pagar(self):
        return self.cantidad * self.producto.precio
    
    def tomar_pago_final(self):
        return self.total_a_pagar()
    
  
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    productos = models.ManyToManyField(OrderProducto)
    start_date = models.DateField   (auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered= models.BooleanField (default=False)
    direccion_factura  = models.ForeignKey('DireccionFactura' , on_delete= models.SET_NULL, blank=True ,  null=True)
    pago  = models.ForeignKey('Pago' , on_delete= models.SET_NULL, blank=True ,  null=True)
    
     

    def __str__(self):
        return self.user.username
    
    def get_total (self):
        total = 0
        for order_producto in self.productos.all():
            total += order_producto.tomar_pago_final()
        return total
        
class DireccionFactura (models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
     direccion = models.CharField(max_length=100)
     apartamento = models.CharField(max_length=100)
     pais = CountryField(multiple=False)
     zip = models.CharField(max_length=100)
     opcion_de_pago = models.CharField(max_length=100)
     telefono = models.IntegerField()
     
     def __str__ (self):
        return self.user.username

class Pago(models.Model):
    stripe_charge_id =  models.CharField(max_length=50)    
    user =  models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL, blank=True , null = True)
    amount  = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__ ( self):
        return self.user.username
    
class Csv(models.Model):
    archivo = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField (auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self) :
        return f"File id: {self.id}"


