from django.db import models
from users.models import User
from utils.models import TypeDocument, Ubigeo

# Create your models here.
class Supervisor(models.Model):
  user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
  code=models.CharField('Codigo', unique=True, max_length=10)
  table=models.CharField('Mesa', max_length=10)#mesa
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Supervisor'
    verbose_name_plural='Supervisors'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.user.username} - {self.table}'

class Zone(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=10)
  description=models.CharField('Descripcion', max_length=255)
  supervisor=models.ForeignKey(Supervisor, on_delete=models.DO_NOTHING)
  status=models.BooleanField('Estado', default=True)

  class Meta:
    verbose_name='Zone'
    verbose_name_plural='Zones'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

class Promoter(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=10)
  user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
  zone=models.OneToOneField(Zone, on_delete=models.CASCADE, null=True)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Promoter'
    verbose_name_plural='Promoters'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return self.code

class Quota(models.Model):
  anio=models.IntegerField('Año')
  mes=models.CharField('Mes', max_length=2)
  periodo=models.CharField('Periodo',max_length=7)
  quota=models.DecimalField('Cuota', max_digits=13, decimal_places=3)
  zone=models.ForeignKey(Zone, on_delete=models.CASCADE)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Quota'
    verbose_name_plural='Quotas'
    ordering=['anio','mes']
    indexes=[
      models.Index(fields=['anio']),
      models.Index(fields=['mes']),
      models.Index(fields=['periodo']),
    ]

  def __str__(self):
    return f'{self.periodo} - {self.quota} - {self.zone.description}'

class Level(models.Model):
  code=models.CharField('Codigo', max_length=10)
  description=models.CharField('Descripcion', max_length=255)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Level'
    verbose_name_plural='Levels'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

class Employee(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  type_document=models.ForeignKey(TypeDocument, on_delete=models.CASCADE)
  number_document=models.CharField('Numero Documento', max_length=254, blank=True, null=True)
  phone=models.CharField('Telefono', max_length=254, blank=True, null=True)
  avatar=models.ImageField('Imagen de perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=200,blank=True, null=True)
  address=models.CharField('Direccion', max_length=254, blank=True, null=True)
  ubigeo=models.ForeignKey(Ubigeo, on_delete=models.DO_NOTHING)
  level=models.ForeignKey(Level, on_delete=models.DO_NOTHING)

  class Meta:
    verbose_name='Employee'
    verbose_name_plural='Employees'
    ordering=['user']
    indexes=[
      models.Index(fields=['user']),
    ]

  def __str__(self):
    return f'{self.user} - {self.type_document.description} - {self.number_document}'
