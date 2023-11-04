from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import TypeDocument, Ubigeo, TypeInvoice, Period

# Register your models here.
class TypeDocumentAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','alias','description']
  list_filter=['id','code','alias','description']
  search_fields=['code','alias','description']

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

admin.site.register(TypeDocument, TypeDocumentAdmin)

class UbigeoAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','region','city','district']
  list_filter=['id','code','region','city','district']
  search_fields=['code','region','city','district']

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

admin.site.register(Ubigeo, UbigeoAdmin)

class TypeInvoiceAdmin(ImportExportMixin, admin.ModelAdmin):
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

admin.site.register(TypeInvoice, TypeInvoiceAdmin)

class PeriodAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','period','year','month']
  list_filter=['id','period','year','month']
  search_fields=['period','year','month']

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

admin.site.register(Period, PeriodAdmin)