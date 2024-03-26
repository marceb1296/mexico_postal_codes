from django.contrib import admin

from .models import PostalCode

# Register your models here.


class PostalCodeAdmin(admin.ModelAdmin):

    list_display = ["pk", "d_codigo", "d_estado", "d_ciudad",
                    "c_mnpio", "id_asenta_cpcons", "d_asenta"]
    search_fields = ["d_codigo", "d_estado", "d_ciudad", "c_mnpio", "d_asenta"]


admin.site.register(PostalCode, PostalCodeAdmin)
