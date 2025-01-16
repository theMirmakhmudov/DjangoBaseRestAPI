from django.contrib import admin
from .models import Book, Category

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_per_page = 5

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 5