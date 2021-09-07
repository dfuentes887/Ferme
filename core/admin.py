from django.contrib import admin
from .models import Marca , Producto, OrderProducto, Order , DireccionFactura, Pago , Csv, TipoProducto , TipoFamilia, Proveedor

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","marca"]
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","start_date","ordered_date","ordered"]
class OrderProductoAdmin(admin.ModelAdmin):
    list_display = ["producto"]
class DireccionFacturaAdmin(admin.ModelAdmin):
    list_display = ["user", "pais", "direccion","telefono"]
class OrderProductoAdmin(admin.ModelAdmin):
    list_display = ["producto"]
class PagoAdmin(admin.ModelAdmin):
    list_display = ["user" ,"amount","timestamp"]

class CsvAdmin(admin.ModelAdmin):
    list_display = ["id","archivo" ,"activated", "uploaded"]
    
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ["id","SKU" ,"nombre"]
class TipoFamiliaAdmin(admin.ModelAdmin):
    list_display = ["id","codigo" ,"nombre", "tipo"]
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "telefono", "rubro", "codigo"]
   

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(OrderProducto, OrderProductoAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DireccionFactura, DireccionFacturaAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Csv, CsvAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(TipoFamilia, TipoFamiliaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)