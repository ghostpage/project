from django.contrib import admin
from secureweb.models import Web, Kelompok
# Register YOur models here.

class InfoWeb(admin.ModelAdmin):
    list_display = ['nama', 'ling', 'tipe', 'keamanan_id']
    search_fields = ['nama', 'ling', 'tipe']
    list_filter = ('keamanan_id',)
    list_per_page = 4

admin.site.register(Web, InfoWeb)
admin.site.register(Kelompok)