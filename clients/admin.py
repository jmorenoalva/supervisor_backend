from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import TypeClient, Client, SitesClient, Contact

# Register your models here.
class TypeClientAdmin(ImportExportMixin, admin.ModelAdmin):
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

admin.site.register(TypeClient, TypeClientAdmin)

class ClientAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','type_client','type_document','nro_document','company_name','fiscal_address','ubigeo']
  list_filter=['id','code','type_client','type_document','nro_document','company_name','fiscal_address','ubigeo']
  search_fields=['code','type_client','type_document','nro_document','company_name','fiscal_address','ubigeo']

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

admin.site.register(Client, ClientAdmin)

class SitesClientAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','client','code','commercial_name','address','ubigeo','promoter']
  list_filter=['id','client','code','commercial_name','address','ubigeo','promoter']
  search_fields=['client','code','commercial_name','address','ubigeo','promoter']

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

admin.site.register(SitesClient, SitesClientAdmin)

class ContactAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','sites_client','item','name','phone','email']
  list_filter=['id','sites_client','item','name','phone','email']
  search_fields=['sites_client','item','name','phone','email']

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

admin.site.register(Contact, ContactAdmin)