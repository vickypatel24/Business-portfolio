from django.contrib import admin
from .models import Member, Products, Product_details


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'age',)

admin.site.register(Member, MemberAdmin)
admin.site.register(Products)
admin.site.register(Product_details)