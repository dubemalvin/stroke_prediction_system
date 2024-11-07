from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('name','gender','stroke_predictions')
admin.site.register(Data)