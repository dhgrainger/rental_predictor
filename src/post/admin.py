from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Post, City
class MyCompanyAdmin(admin.ModelAdmin):
 model = City
 list_display = ('name', 'slug', 'description', 'pe_ratio',)
admin.site.register(City, MyCompanyAdmin)
