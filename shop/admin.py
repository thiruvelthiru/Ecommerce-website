from django.contrib import admin
from .models import *
# Register your models here.


"""class CatagoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
    admin.site.register(Catagory,CatagoryAdmin)
    """   # when to use to acces the code for django admin add specfi


admin.site.register(Catagory)
admin.site.register(Product)