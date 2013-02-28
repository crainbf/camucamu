from django.contrib import admin
from camucamu.apps.books.models import Author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'pages', 'date_finished', 'user',)
    list_filter = ('title',)
    ordering = ('title',)
    filter_horizontal = ('authors',)
    ordering = ('user', '-date_finished',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
