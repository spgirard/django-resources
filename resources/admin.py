### faq app admin


from django.contrib import admin
#   our models
from .models import Resource_Category, Resource


@admin.register(Resource_Category)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    prepopulated_fields = {'slug': ('category',)}

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'category']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}    
    list_editable = ['category']