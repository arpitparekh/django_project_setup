from django.contrib import admin
from . import models

@admin.register(models.Product)
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
    filter_horizontal = ()
    list_filter = ('name','price','stock')
    fieldsets = ()
