from django.contrib import admin
from tasks.models import Category, Task

@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')
    list_display_links = ('title', 'description', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

