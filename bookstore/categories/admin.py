from django.contrib import admin
from django.contrib.admin import ModelAdmin

from categories.models import Category

class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
