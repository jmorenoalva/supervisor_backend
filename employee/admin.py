from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Zone, Supervisor, Promoter, Quota, Level, Employee

# Register your models here.
class SupervisorAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','user', 'code', 'table']
  list_filter=['id','user', 'code','table']
  search_fields=['user', 'code', 'table']

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

admin.site.register(Supervisor,SupervisorAdmin)

class ZoneAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','description','supervisor']
  list_filter=['id','code','description','supervisor']
  search_fields=['code','description','supervisor']

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

admin.site.register(Zone,ZoneAdmin)

class PromoterAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','user','zone']
  list_filter=['id','code','user','zone']
  search_fields=['code','user','zone']
  autocomplete_fields=('user','zone')

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

admin.site.register(Promoter,PromoterAdmin)

class QuotaAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','anio','mes','periodo','quota','zone']
  list_filter=['id','anio','mes','periodo','quota','zone']
  search_fields=['anio','mes','periodo','quota','zone']

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

admin.site.register(Quota,QuotaAdmin)

class LevelAdmin(ImportExportMixin, admin.ModelAdmin):
   list_display=['id', 'code', 'description']
   list_filter=['id', 'code', 'description']
   search_fields=['code', 'description']

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

admin.site.register(Level,LevelAdmin)

class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','user','type_document','number_document','phone','address','ubigeo']
  list_filter=['id','user','type_document','number_document','phone','address','ubigeo']
  search_fields=['user','type_document','number_document','phone','address','ubigeo']
  autocomplete_fields = ('user','type_document','ubigeo')

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

admin.site.register(Employee,EmployeeAdmin)

