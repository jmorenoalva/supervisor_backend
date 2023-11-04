from django.db import models

# Create your models here.
class TypeDocument(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=2)
  alias=models.CharField('Alias', max_length=10)
  description=models.CharField('Descripcion', max_length=254, blank=True)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='TypeDocument'
    verbose_name_plural='TypeDocuments'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
      models.Index(fields=['description']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

  def to_dict(self):
    return {
      "id": self.id,
      "code": self.code,
      "alias": self.alias,
      "description":self.description,
      "status":self.status,
    }

class Ubigeo(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=6)
  region=models.CharField('Departamento', max_length=100)
  city=models.CharField('Provincia', max_length=100)
  district=models.CharField('Distrito', max_length=100)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Ubigeo'
    verbose_name_plural='Ubigeos'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
      models.Index(fields=['region']),
      models.Index(fields=['city']),
      models.Index(fields=['district'])
    ]

  def __str__(self):
    return f'{self.code} - {self.region} - {self.city} - {self.district}'

  def to_dict(self):
    return {
      "id": self.id,
      "code": self.code,
      "region": self.region,
      "city":self.city,
      "district":self.district,
      "status":self.status,
    }

class TypeInvoice(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=2)
  description=models.CharField('Descripcion', max_length=100)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='TypeInvoice'
    verbose_name_plural='TypesInvoices'
    ordering=['code']
    indexes=[
      models.Index(fields=['code'])
    ]

  def __str__(self):
    return self.code

  def to_dict(self):
    return {
      "id": self.id,
      "code": self.code,
      "description": self.description,
      "status":self.status,
    }

class Period(models.Model):
  period=models.CharField('Periodo', unique=True, max_length=7)
  year=models.IntegerField('Año')
  month=models.CharField('Mes', max_length=2)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Period'
    verbose_name_plural='Periods'
    ordering=['period']
    indexes=[
      models.Index(fields=['period'])
    ]

  def __str__(self):
    return self.period

  def to_dict(self):
    return {
      "id": self.id,
      "period": self.period,
      "year": self.year,
      "month":self.month,
      "status":self.status,
    }