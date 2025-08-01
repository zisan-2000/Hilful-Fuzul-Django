from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at',)
    readonly_fields = ('name', 'email', 'phone_number', 'message', 'created_at')
