from django.contrib import admin
from .models import Publisher

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'books_count')
    search_fields = ('name',)
