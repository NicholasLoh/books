from django.contrib import admin
from .models import Item

# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'stream', 'price')
    list_display_links = ('user', 'title')
    list_per_page = 50

admin.site.register(Item, ItemsAdmin)