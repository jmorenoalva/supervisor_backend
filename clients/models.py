from django.db import models
from utils.models import TypeDocument, Ubigeo
from employee.models import Promoter

# Create your models here.
class TypeClient(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=4)
  description=models.CharField('Descripcion', max_length=255)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Type_client'
    verbose_name_plural='Type_clients'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

class Client(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=20)
  type_client=models.ForeignKey(TypeClient, on_delete=models.DO_NOTHING,)
  type_document=models.ForeignKey(TypeDocument, on_delete=models.DO_NOTHING,)
  nro_document=models.CharField('Codigo', unique=True, max_length=20)
  company_name=models.CharField('Razon_Social', max_length=255)
  fiscal_address=models.CharField('Domicilio_Fiscal', max_length=255)
  ubigeo=models.ForeignKey(Ubigeo, on_delete=models.DO_NOTHING,)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Client'
    verbose_name_plural='Clients'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.company_name}  - {self.type_client.description} - {self.type_document.alias} - {self.nro_document} - {self.ubigeo.code}'

class SitesClient(models.Model):
  client=models.ForeignKey(Client,on_delete=models.DO_NOTHING,)
  code=models.CharField('Codigo', max_length=4)
  commercial_name=models.CharField('Nombre_Comercial', max_length=255)
  address=models.CharField('Direccion', max_length=255)
  ubigeo=models.ForeignKey(Ubigeo, on_delete=models.DO_NOTHING,)
  promoter=models.ForeignKey(Promoter, on_delete=models.DO_NOTHING)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Sites_client'
    verbose_name_plural='Sites_clients'
    ordering=['client','code']
    indexes=[
      models.Index(fields=['code']),
      models.Index(fields=['commercial_name']),
    ]

  def __str__(self):
    return self.code

class Contact(models.Model):
  sites_client=models.ForeignKey(SitesClient, on_delete=models.DO_NOTHING,)
  item=models.IntegerField('Item')
  name=models.CharField('Nombre', max_length=255)
  phone=models.CharField('Telefono', max_length=255)
  email=models.CharField('Correo', max_length=255)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Contact'
    verbose_name_plural='Contacts'
    ordering=['sites_client','item']
    indexes=[
      models.Index(fields=['item']),
      models.Index(fields=['name']),
    ]

  def __str__(self):
    return self.item