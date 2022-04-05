from django.contrib import admin
from .models import Document, Object


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ['doc_name']


class ObjectAdmin(admin.ModelAdmin):
    search_fields = ['doc_class']


admin.site.register(Document, DocumentAdmin)
admin.site.register(Object, ObjectAdmin)
