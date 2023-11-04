from django.contrib import admin
from import_export.admin import ImportExportMixin
from import_export import resources
from .models import User

# Register your models here.
class UserResource(resources.ModelResource): #con esta clase defino que campos exportar al excel
  class Meta:
      model = User
      fields = ('username', 'names', 'last_names', 'email', 'is_superuser')

class UserAdmin(ImportExportMixin, admin.ModelAdmin): # con esta clase hace que se pueda hacer una busqueda por los campos que listo y se puede exportar a excel
  list_display=['id','username','names','last_names','email','is_superuser']
  list_filter=['id','username','names','last_names','email','is_superuser']
  search_fields=['username','names','last_names','email','is_superuser']
  resource_class = UserResource

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

  export_to_excel.short_description='Exportar a Excel'
  actions=[export_to_excel]

admin.site.register(User,UserAdmin)