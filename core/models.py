
from django.db import models

# MODELO DE PROYECTO DESCUETNO 
# Create your models here.

#Tipo Usuario
class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombretipousuario = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return '{}' .format(self.nombretipousuario)
    class Meta:
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipo Usuario"

#Usuario      
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    idtipousuario = models.ForeignKey(TipoUsuario,to_field='id',on_delete=models.CASCADE)
    username = models.CharField(max_length=30,null=True,unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return '{}' .format(self.username)
    class Meta:
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipo Usuario"
        
        
    

    
    

#Industria Empresa Titular
class IndustriaEmpresaTitular(models.Model):
    id = models.AutoField(primary_key=True)
    nombreindustria = models.CharField(max_length=30)
    descripcionindustria = models.CharField(max_length=100)
    def __str__(self):
            return '{} '.format(self.nombreindustria)
    
    class Meta:
        verbose_name = "IdustriaEmpresaTitular"
        verbose_name_plural = "IdustriaEmpresaTitular"
        
#Empresa Titular
class EmpresaTitular(models.Model):
    id = models.AutoField(primary_key=True)
    idindustriaempresatitular = models.ForeignKey(IndustriaEmpresaTitular,to_field='id',on_delete=models.CASCADE)
    nombreempresatitular = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)        
    def __str__(self):
            return '{} '.format(self.nombreempresatitular)
    
    class Meta:
        verbose_name = "Empresa Titular"
        verbose_name_plural = "Empresa Titular"
    
#Producto Empresa Titular
class ProductoEmpresaTitular(models.Model):
    id = models.AutoField(primary_key=True)
    idempresatitular = models.ForeignKey(EmpresaTitular,to_field='id',on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
            return '{} '.format(self.nombreproducto)
    
    class Meta:
        verbose_name = "Produco Empresa Titular"
        verbose_name_plural = "Producto Empresa Titular"
        
#Categoria Beneficio
class CategoriaBeneficio(models.Model):
    id = models.AutoField(primary_key=True)
    nombrecategoriabeneficio = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
            return '{} '.format(self.nombrecategoriabeneficio)
    
    class Meta:
        verbose_name = "Categoria Beneficio"
        verbose_name_plural = "Categoria Beneficio"
        

#Empresa Beneficio
class EmpresaBeneficio(models.Model):
    id = models.AutoField(primary_key=True)
    nombreempresabeneficio = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
            return '{}'.format(self.nombreempresabeneficio)
    
    class Meta:
        verbose_name = "Empresa Beneficio"
        verbose_name_plural = "Empresa Beneficio"
        
#Empresa Titular Beneficio
class EmpresaTitularBeneficio(models.Model):
    id = models.AutoField(primary_key=True)
    idproductoempresatitular = models.ForeignKey(ProductoEmpresaTitular,to_field='id',on_delete=models.CASCADE)
    idcategoriabeneficio = models.ForeignKey(CategoriaBeneficio,to_field='id',on_delete=models.CASCADE)
    idempresabeneficio = models.ForeignKey(EmpresaBeneficio,to_field='id',on_delete=models.CASCADE)
    nombrebeneficio = models.CharField(max_length=30)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    checklu = models.BooleanField()
    checkma = models.BooleanField()
    checkmi = models.BooleanField()
    checkju = models.BooleanField()
    checkvi = models.BooleanField()
    checksa = models.BooleanField()
    checkdo = models.BooleanField()
    def __str__(self):
            return '{}'.format(self.nombrebeneficio)
    
    class Meta:
        verbose_name = "Empresa Titular Beneficio"
        verbose_name_plural = "Empresa Titular Beneficio"
    
#Categoria Preferencia Personal
class CategoriaPreferenciaPersonal(models.Model):
    id = models.AutoField(primary_key=True)
    nombrecategoriapreferencia = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
            return '{}'.format(self.nombrecategoriapreferencia)
    
    class Meta:
        verbose_name = "Categoria Preferencia Personal"
        verbose_name_plural = "Categoria Preferencia Personal"
        
        

#Preferencia Personal
class PreferenciaPersonal(models.Model):
    id= models.AutoField(primary_key=True)
    idcategoriapreferenciapersonal = models.ForeignKey(CategoriaPreferenciaPersonal,to_field='id',on_delete=models.CASCADE)
    nombrepreferenciapersonal = models.CharField(max_length=30,null=True,unique=True)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.nombrepreferenciapersonal)
    
    class Meta:
        verbose_name = " Preferencia Personal"
        verbose_name_plural = "Preferencia Personal"


#Usuario Producto Empresa Titular
class UsuarioProductoEmpresaTitular(models.Model):
    id = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario,to_field='id',on_delete=models.CASCADE)
    idproductoempresatitular = models.ForeignKey(ProductoEmpresaTitular,to_field='id',on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.id)
    
    class Meta:
        verbose_name = "Usuario Producto Empresa Titular"
        verbose_name_plural = "Usuario Producto Empresa Titular"        

#Usuario Preferencia
class UsuarioPreferencia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario,to_field='username',on_delete=models.CASCADE,related_name='usuarios')
    preferencia = models.OneToOneField(PreferenciaPersonal,to_field='nombrepreferenciapersonal',on_delete=models.CASCADE,related_name='preferencias')
    def __str__(self):
        return '{}'.format(self.id)
    
    class Meta:
        verbose_name = "Usuario Preferencia"
        verbose_name_plural = "Usuario Preferencia"