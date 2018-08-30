from django.contrib import admin

# Register your models here.
from except_catcher.models import ExceptionReport

admin.site.register(ExceptionReport)
