from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Unit, ActiveIngredient, Presentation, Product

# Register your models here.
class UnitAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','description']
  list_filter=['id','code','description']
  search_fields=['code','description']

  def export_to_excel(self,request,queryset):
    # Obtener la configuración de exportación del modelo
    export_format = self.get_export_formats()[0]()
    export_data = export_format.export_data(queryset)

    # Configurar la respuesta HTTP
    response = HttpResponse(content_type=export_format.get_content_type())
    response['Content-Disposition'] = 'attachment; filename="tu_archivo.xlsx"'

    # Escribir los datos de exportación en la respuesta
    response.write(export_data)

    return response

admin.site.register(Unit, UnitAdmin)

class ActiveIngredientAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','description']
  list_filter=['id','code','description']
  search_fields=['code','description']

  def export_to_excel(self,request,queryset):
    # Obtener la configuración de exportación del modelo
    export_format = self.get_export_formats()[0]()
    export_data = export_format.export_data(queryset)

    # Configurar la respuesta HTTP
    response = HttpResponse(content_type=export_format.get_content_type())
    response['Content-Disposition'] = 'attachment; filename="tu_archivo.xlsx"'

    # Escribir los datos de exportación en la respuesta
    response.write(export_data)

    return response

admin.site.register(ActiveIngredient, ActiveIngredientAdmin)

class PresentationAdmin(ImportExportMixin,admin.ModelAdmin):
  list_display=['id','code','description']
  list_filter=['id','code','description']
  search_fields=['code','description']

  def export_to_excel(self,request,queryset):
    # Obtener la configuración de exportación del modelo
    export_format = self.get_export_formats()[0]()
    export_data = export_format.export_data(queryset)

    # Configurar la respuesta HTTP
    response = HttpResponse(content_type=export_format.get_content_type())
    response['Content-Disposition'] = 'attachment; filename="tu_archivo.xlsx"'

    # Escribir los datos de exportación en la respuesta
    response.write(export_data)

    return response

admin.site.register(Presentation, PresentationAdmin)

class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['code','description','unit', 'presentation', 'resolution', 'indication']
  list_filter=['code','description','unit', 'presentation', 'resolution', 'indication']
  search_fields=['code','description','unit.description', 'presentation.description', 'resolution', 'indication']

  def export_to_excel(self,request,queryset):
    # Obtener la configuración de exportación del modelo
    export_format = self.get_export_formats()[0]()
    export_data = export_format.export_data(queryset)

    # Configurar la respuesta HTTP
    response = HttpResponse(content_type=export_format.get_content_type())
    response['Content-Disposition'] = 'attachment; filename="tu_archivo.xlsx"'

    # Escribir los datos de exportación en la respuesta
    response.write(export_data)

    return response

admin.site.register(Product, ProductAdmin)
