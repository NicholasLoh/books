from django.contrib import admin
from .models import Profile, Inquiry

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
# Register your models here.
admin.site.register(Profile, ProfileAdmin)

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('userId','name', 'email')
    list_display_links = ('userId','name')
    list_per_page = 50

admin.site.register(Inquiry, InquiryAdmin)
