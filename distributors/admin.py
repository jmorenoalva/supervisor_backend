from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Distributor, ProductDistributor, Sales

# Register your models here.
class DistributorAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','code','type_document','nro_document','company_name', 'fiscal_address', 'ubigeo', 'status']
  list_filter=['id','code','type_document','nro_document','company_name', 'fiscal_address', 'ubigeo', 'status']
  search_fields=['code','type_document','nro_document','company_name', 'fiscal_address', 'ubigeo']

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

admin.site.register(Distributor, DistributorAdmin)

class ProductDistributorAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['code', 'description', 'distributor', 'product']
  list_filter=['code', 'description', 'distributor', 'product']
  search_fields=['code', 'description', 'distributor', 'product']

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

admin.site.register(ProductDistributor, ProductDistributorAdmin)

class SalesAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display=['id','distributor','date','client','code_client','company_name','commercial_name','district','sites_client','ubigeo','product','code_product','code_product_distributor_first','code_product_distributor_second','description_product','amount','value','price','promoter','code_promoter','name_promoter','code_vendedor','type_invoice','serie_invoice','nro_invoice','period']
  list_filter=['id','distributor','date','client','code_client','company_name','commercial_name','district','sites_client','ubigeo','product','code_product','code_product_distributor_first','code_product_distributor_second','description_product','amount','value','price','promoter','code_promoter','name_promoter','code_vendedor','type_invoice','serie_invoice','nro_invoice','period']
  search_fields=['distributor','date','client','code_client','company_name','commercial_name','district','sites_client','ubigeo','product','code_product','code_product_distributor_first','code_product_distributor_second','description_product','amount','value','price','promoter','code_promoter','name_promoter','code_vendedor','type_invoice','serie_invoice','nro_invoice','period']

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

admin.site.register(Sales, SalesAdmin)