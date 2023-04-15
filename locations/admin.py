from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'address')
