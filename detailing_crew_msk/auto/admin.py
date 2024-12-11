from django.contrib import admin
# from unfold.admin import ModelAdmin
from .models import Auto


@admin.register(Auto)
# class AutoAdmin(ModelAdmin):
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
