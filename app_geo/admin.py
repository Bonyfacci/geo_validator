from django.contrib import admin

from app_geo.models import Address, Request


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cad_number', 'latitude', 'longitude', 'created', 'updated', )
    search_fields = ['cad_number', ]


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'address', 'response', 'created', 'updated', )
    list_filter = ['response', ]
