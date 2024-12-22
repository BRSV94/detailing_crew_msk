from django.contrib import admin
from .models import Auto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model',
        'plate'
    )
    list_filter = (
        'brand',
        'model',
        'plate'
    )
