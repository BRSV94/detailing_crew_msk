from typing import Any
from django.contrib import admin
from django.forms.widgets import SplitDateTimeWidget, SelectDateWidget, DateTimeBaseInput, DateTimeInput
# from unfold.admin import ModelAdmin
from detailing.models import (Appointment, ClientUser, FlawTitle,
                     Order, StaffUser, Work)

from autos.models import Auto


@admin.register(ClientUser)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'last_name',
        'first_name',
        'orders',
        'autos',
        'friendly',
        'solvent',
    )
    list_filter = (
        'phone_number',
        'last_name',
        'autos',
        'friendly',
        'solvent',
        'next_visit',
    )
    list_display_links = (
        'last_name',
        'first_name',
        'orders',
        # 'autos',
    )
    search_fields = (
        'phone_number',
        'last_name',
        'first_name',
    )

    @admin.display(description='Последний заказ-наряд клиента')
    def orders(self, obj):
        return obj.orders.order_by('-date').first()

    @admin.display(description='Автомобили клиента')
    def autos(self, obj):
        autos = list(obj.autos.all())
        result = ''
        for auto in autos:
            result += f'{auto}, '
        return result[:-2]


@admin.register(StaffUser)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'last_name',
        'first_name',
        'username',
        'orders',
    )
    list_filter = (
        'phone_number',
        'last_name',
    )
    list_display_links = (
        'last_name',
        'first_name',
    )

    @admin.display(description='Заказ-наряды сотрудника')
    def orders(self, obj):
        obj.orders


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'description',
    )


# class FlawInline(admin.TabularInline):
#     # model = Order.works.through
#     model = Order.flaws
#     extra = 0


@admin.register(Order)
# class OrderAdmin(ModelAdmin):
class OrderAdmin(admin.ModelAdmin):
    list_display =  (
        'client',
        'auto',
        'executor',
        'price',
        'date',
        'is_done',
    )
    list_filter = (
        'client',
        'auto',
        'executor',
        'works',
        'date',
        'is_done',
    )
    filter_vertical = (
        'works',
    )
    list_display_links = (
        'client',
        'auto',
    )
    readonly_fields = (
        'price',
    )
    search_fields = (
        # 'client',
        # 'auto',
        # 'executor',
        # 'works',
        # 'date',
        # 'is_done',
    )


@admin.register(FlawTitle)
class FlawAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Appointment)
# class AppointmentAdmin(ModelAdmin):
class AppointmentAdmin(admin.ModelAdmin):
    list_display =  (
        'client',
        'auto',
        'visit_time',
    )
    list_filter = (
        'client',
        'auto',
        'visit_time',
    )
    list_display_links = (
        'client',
        'auto',
    )
    search_fields = (
        'client',
        'visit_time'
    )

    # class Meta:
    #     model = Appointment
    #     widgets = {
    #         'visit_time': DateTimeInput,
    #         # SelectDateWidget, DateTimeBaseInput, DateTimeInput
    #     }