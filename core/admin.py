from django.contrib import admin


# Register your models here.

#Tipo Usuario admin
from core.models import TipoUsuario
class TipoUsuarioadmin(admin.ModelAdmin):
    list_display = ('id','nombretipousuario','descripcion')  
admin.site.register(TipoUsuario,TipoUsuarioadmin)

#Usuario admin
from core.models import Usuario
class Usuarioadmin(admin.ModelAdmin):
    list_display = ('id','idtipousuario','username','password')
admin.site.register(Usuario,Usuarioadmin)

#Industria Empresa Titular admin
from core.models import IndustriaEmpresaTitular
class IndustriaEmpresaTitularadmin(admin.ModelAdmin):
    list_display = ('id','nombreindustria','descripcionindustria')
admin.site.register(IndustriaEmpresaTitular,IndustriaEmpresaTitularadmin)

#Empresa Titular admin
from core.models import EmpresaTitular
class EmpresaTitularadmin(admin.ModelAdmin):
    list_display = ('id','idindustriaempresatitular','nombreempresatitular','descripcion')
admin.site.register(EmpresaTitular,EmpresaTitularadmin)

#Producto Empresa Titular admin
from core.models import ProductoEmpresaTitular
class ProductoEmpresaTitularadmin(admin.ModelAdmin):
    list_display = ('id','idempresatitular','nombreproducto','descripcion')
admin.site.register(ProductoEmpresaTitular,ProductoEmpresaTitularadmin)

#Categoria Beneficio admin
from core.models import CategoriaBeneficio
class CategoriaBeneficioadmin(admin.ModelAdmin):
    list_display = ('id','nombrecategoriabeneficio','descripcion')
admin.site.register(CategoriaBeneficio,CategoriaBeneficioadmin)

#Empresa Beneficio admin
from core.models import EmpresaBeneficio
class EmpresaBeneficioadmin(admin.ModelAdmin):
    list_display = ('id','nombreempresabeneficio','descripcion')
admin.site.register(EmpresaBeneficio,EmpresaBeneficioadmin)

#Empresa Titular Beneficio admin
from core.models import EmpresaTitularBeneficio
class EmpresaTitularBeneficioadmin(admin.ModelAdmin):
    list_display = ('id','idproductoempresatitular','idcategoriabeneficio','idempresabeneficio','nombrebeneficio','fechainicio','fechatermino','checklu','checkma','checkmi','checkju','checkvi','checksa','checkdo')
admin.site.register(EmpresaTitularBeneficio,EmpresaTitularBeneficioadmin)

#Categoria Preferencia Personal admin
from core.models import CategoriaPreferenciaPersonal
class CategoriaPreferenciaPersonaladmin(admin.ModelAdmin):
    list_display = ('id','nombrecategoriapreferencia','descripcion')
admin.site.register(CategoriaPreferenciaPersonal,CategoriaPreferenciaPersonaladmin)

#Preferencia Personal admin
from core.models import PreferenciaPersonal
class PreferenciaPersonaladmin(admin.ModelAdmin):
    list_display = ('id','idcategoriapreferenciapersonal','nombrepreferenciapersonal','descripcion')
admin.site.register(PreferenciaPersonal,PreferenciaPersonaladmin)

#Usuario Producto Empresa Titular admin
from core.models import UsuarioProductoEmpresaTitular
class UsuarioProductoEmpresaTitularadmin(admin.ModelAdmin):
    list_display = ('id','idusuario','idproductoempresatitular')
admin.site.register(UsuarioProductoEmpresaTitular,UsuarioProductoEmpresaTitularadmin)

#suario Preferencia
from core.models import UsuarioPreferencia
class UsuarioPreferenciaadmin(admin.ModelAdmin):
    list_display = ('id','usuario','preferencia')
admin.site.register(UsuarioPreferencia,UsuarioPreferenciaadmin)