from django.contrib import admin
from .models import  Blog 

admin.site.register(Blog)
admin.AdminSite.app_index_template = "admin/blog/add-blog.html"
