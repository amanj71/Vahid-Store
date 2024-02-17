from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

#@admin.register(models.BackgrounFigure)
#class ProductAdmin(admin.ModelAdmin):
#    list_display = ['title']