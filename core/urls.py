from django.urls import path
from .views import  *

from core.user.views import UserCreateView
app_name = 'core'

urlpatterns = [
     path('', Index, name= "Index"),
     
     path('registro/', registro, name= "registro"),
     path('agregar-productos/', agregar_producto, name= "agregar_producto"),
     path('menu-productos/', menu_productos, name= "menu-productos"),
     path('listar-productos/', listar_productos, name= "listar-productos"),
     path('modificar-productos/<id>/', modificar_producto, name= "modificar-productos"),
     path('modificar-usuarios/<id>/', modificar_user, name= "modificar-usuarios"),
     
     path('eliminar-productos/<id>/', eliminar_productos, name= "eliminar-productos"),
     path('eliminar-usuario/<id>/', eliminar_usuario, name= "eliminar-usuario"),
     
     

     path('producto/<slug>/', ProductoVer.as_view(), name= "producto"),
     path('add-to-cart/<slug>/',add_to_cart, name = "add-to-cart"),
     path('remove-from-cart/<slug>/',remove_from_cart, name = "remove-from-cart"),
     path('remove-item-from-cart/<slug>/', remove_single_from_cart,
          name='remove-single-from-cart'),
     path('add-single-to-cart/<slug>/', add_single_to_cart,
          name='add-single-to-cart'),
     path('carrito/', carrito.as_view(), name= "carrito"),
     path('pdf', OrdenPDF.as_view(), name= "pdf-view"),
     path('pdf-descargar', DownloadPDF.as_view(), name= "pdf-download"),
     path('finalizar_pago/', finalizar_pago, name= "finalizar-pago"),
     path('carro/', carro, name= "carro"),
     path('checkout/', CheckoutView.as_view(), name= "checkout"),
     path('pagar/<opcion_de_pago>', VistaPago.as_view(), name= "pago"),
     path('producto/subir_archivo', upload_file_view, name= "subir_archivo"),
     path('listado', listado_productos, name= "listado-producto"),
     path('personas/listado', listado_personas, name= "listado-personas"),
     path('logout', logout, name= "logout"),
     path('pago-realizado', pago_realizado, name= "pago-realizado"),
     path('producto/invoice/pdf/<int:pk>', SaleInvoicePdfView.as_view(), name= "sale_invoice_pdf"),
     path('checkout/finalizarCompra/', finalizarCompra, name= "finalizar-compra"),
     path('registro-usuario', UserCreateView.as_view(), name= "registro-usuario"),
     #Crud grupos
     path ('lista-grupos', listaGrupos, name = 'listado-groups') ,
     path ('lista-grupos-agregar', listaGrupos_add, name = 'groups-add') ,
     path('lista-grupos-modificar/<id>/', listaGrupos_change, name= "listaGrupos_change"),
     path('eliminar-grupo/<id>/', listaGrupos_del, name= "eliminar-grupo"),
     #Grupo-Usuario
     path('mostrar-grupo/<id>/', userGroup, name= "userGroup"),
     path('agregar-grupo/<id>/', userGroup_add, name= "userGroup_add"),
     path('delete-grupo/<id>/<name>', userGroup_delete, name= "userGroup_delete"),

     #Proveedor
     path('listar-proveedores', listar_proveedores, name= "listar_proveedores"),
     path('agregar-proveedores/', agregar_proveedores, name= "agregar_proveedores"),
     path('modificar-proveedores/<id>/', modificar_proveedores, name= "modificar_proveedores"),
     path('eliminar-proveedores/<id>/', eliminar_proveedores, name= "eliminar_proveedores"),
     path('como-usar', manual_de_usuario, name= "manual_de_usuario"),
]
