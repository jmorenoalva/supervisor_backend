from django.db import models
from utils.models import TypeDocument, Ubigeo, TypeInvoice, Period
from product.models import Product
from clients.models import Client, SitesClient
from employee.models import Promoter

# Create your models here.
class Distributor(models.Model):
  code=models.CharField('Codigo', max_length=4)
  type_document=models.ForeignKey(TypeDocument, on_delete=models.DO_NOTHING)
  nro_document=models.CharField('Documento', max_length=20)
  company_name=models.CharField('Razon_social', max_length=255)
  fiscal_address=models.CharField('Domicilio_Fiscal', max_length=255)
  ubigeo=models.ForeignKey(Ubigeo, on_delete=models.DO_NOTHING,)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Distribuitor'
    verbose_name_plural='Distribuitors'
    ordering=['company_name']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.company_name}'

class ProductDistributor(models.Model):
  code=models.CharField('Codigo', max_length=15)
  description=models.CharField('Descripcion', max_length=255)
  distributor=models.ForeignKey(Distributor,on_delete=models.DO_NOTHING)
  product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)

  class Meta:
    verbose_name='ProductDistributor'
    verbose_name_plural='ProductsDistributors'
    ordering=['distributor','description']
    indexes=[
      models.Index(fields=['code']),
      models.Index(fields=['distributor']),
      models.Index(fields=['product']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description} - {self.distributor}'

class Sales(models.Model):
  distributor=models.ForeignKey(Distributor, on_delete=models.DO_NOTHING)
  date=models.DateField()
  client=models.ForeignKey(Client, on_delete=models.DO_NOTHING)
  code_client=models.CharField('Codigo_cliente', max_length=20)
  company_name=models.CharField('Razon_social', max_length=255)
  commercial_name=models.CharField('Nombre_comercial', max_length=255)
  district=models.CharField('Distrito', max_length=50)
  sites_client=models.ForeignKey(SitesClient, on_delete=models.DO_NOTHING)
  ubigeo=models.ForeignKey(Ubigeo, on_delete=models.DO_NOTHING)
  product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
  code_product=models.CharField('Codigo_producto', max_length=10)
  code_product_distributor_first=models.CharField('Codigo_producto_distribuidora_primero', max_length=20)
  code_product_distributor_second=models.CharField('Codigo_producto_distribuidora_segundo', max_length=20, null=True)
  description_product=models.CharField('Descripcion_producto', max_length=255)
  amount=models.IntegerField('Cantidad')
  value=models.DecimalField('Valor', max_digits=14, decimal_places=4)
  price=models.DecimalField('Precio', max_digits=14, decimal_places=4)
  promoter=models.ForeignKey(Promoter, on_delete=models.DO_NOTHING)
  code_promoter=models.CharField('Codigo_promotor', max_length=10)
  name_promoter=models.CharField('Nombre_promotor', max_length=255)
  code_vendedor=models.CharField('Codigo_vendedor', max_length=10)
  type_invoice=models.ForeignKey(TypeInvoice, on_delete=models.DO_NOTHING)
  serie_invoice=models.CharField('Serie_comprobante', max_length=4)
  nro_invoice=models.CharField('Nro_comprobante', max_length=8)
  period=models.ForeignKey(Period, on_delete=models.DO_NOTHING)

  class Meta:
    verbose_name='Sale'
    verbose_name_plural='Sales'
    ordering=['distributor','client']
    indexes=[
      models.Index(fields=['distributor']),
      models.Index(fields=['date']),
      models.Index(fields=['client']),
      models.Index(fields=['code_client']),
      models.Index(fields=['district']),
      models.Index(fields=['sites_client']),
      models.Index(fields=['ubigeo']),
      models.Index(fields=['product']),
      models.Index(fields=['code_product']),
      models.Index(fields=['promoter']),
      models.Index(fields=['period']),
    ]

  def __str__(self):
    return f'{self.distributor} - {self.client} - {self.period}'