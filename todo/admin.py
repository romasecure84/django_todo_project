from django.contrib import admin
from .models import Todo, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'category',
        'title',
        'is_active',
        'cerated_at',
        'updated_at',
    ]
    list_display_links = [
        'pk',
        'category',
        'title',
    ]
    
admin.site.register(Todo, TodoAdmin)
admin.site.register(Category)