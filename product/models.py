from django.db import models

# Create your models here.
class Unit(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=10)
  description=models.CharField('Descripcion', max_length=255)
  status=models.BooleanField('Estado', default=True)

  class Meta:
    verbose_name='Unit'
    verbose_name_plural='Units'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

class ActiveIngredient(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=10)
  description=models.CharField('Descripcion', max_length=255)
  status=models.BooleanField('Estado', default=True)

  class Meta:
    verbose_name='ActiveIngredient'
    verbose_name_plural='ActiveIngredients'
    ordering=['code']
    indexes=[
      models.Index(fields=['code']),
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

class Presentation(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=10)
  description=models.CharField('Descripcion', max_length=255)
  status=models.BooleanField('Estado', default=True)

  class Meta:
    verbose_name='Presentation'
    verbose_name_plural='Presentations'
    ordering=['code']
    indexes=[
      models.Index(fields=['code'])
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'

class Product(models.Model):
  code=models.CharField('Codigo', unique=True, max_length=10)
  description=models.CharField('Descripcion', max_length=255)
  unit=models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
  presentation=models.ForeignKey(Presentation, on_delete=models.DO_NOTHING)
  resolution=models.CharField('Resolution', max_length=255)
  indication=models.CharField('Indication', max_length=255)
  active_ingredient=models.ManyToManyField(ActiveIngredient)
  status=models.BooleanField(default=True)

  class Meta:
    verbose_name='Product'
    verbose_name_plural='Products'
    ordering=['code', 'unit']
    indexes=[
      models.Index(fields=['code'])
    ]

  def __str__(self):
    return f'{self.code} - {self.description}'