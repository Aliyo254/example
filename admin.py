from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'email')


class ElderAdmin(admin.ModelAdmin):
    model = Elder
    list_display = ('user', 'email', 'contact', 'hood')


class ResidentAdmin(admin.ModelAdmin):
    model = Resident
    list_display = ('user', 'email', 'contact', 'hood')


class ControllerAdmin(admin.ModelAdmin):
    model = Controller
    list_display = ('user', 'email', 'contact', 'hood')


class HoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    prepopulated_fields = {'slug': ('name',)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'hood',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(User, UserAdmin)
admin.site.register(Elder, ElderAdmin)
admin.site.register(Resident, ResidentAdmin)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(Hood, HoodAdmin)
admin.site.register(Service, ServiceAdmin)