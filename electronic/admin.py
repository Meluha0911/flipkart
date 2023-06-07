from django.contrib import admin
from .models import *

# Register your models here.
class LaptopModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty']

class MobileModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty']

class TVModelAdmin(admin.ModelAdmin):
    list_display = ['modelname','modelprice','modelqnty']

admin.site.register(LaptopModel,LaptopModelAdmin)
admin.site.register(MobileModel,MobileModelAdmin)
admin.site.register(TVModel,TVModelAdmin)

