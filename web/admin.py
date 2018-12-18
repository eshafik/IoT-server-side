from django.contrib import admin
from .models import Line, Production
# Register your models here.

@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ('line_no',)


@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('line','production_size','production_date')

