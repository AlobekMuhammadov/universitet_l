from django.contrib import admin
from .models import *
# admin.site.register(Yonalish)
# admin.site.register(Fan)
# admin.site.register(Ustoz)


@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    list_display = ('ism','jins','yosh','daraja')
    search_fields = ('ism',)

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_filter = ('aktiv',)
    search_fields = ('nom',)

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_filter = ('yonalish','asosiy')
    search_fields = ('nom',)