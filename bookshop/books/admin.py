from django.contrib import admin

from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_eng', 'price', 'sale', 'author',
        'cat', 'photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'sale')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  

admin.site.register(Books, BooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)