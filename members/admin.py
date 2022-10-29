from django. contrib import admin
from.models import imagedeatails, members
from .models import productdetails

class vegiAdmin(admin.ModelAdmin):
    list_display =('fruits','vegitable')

class products(admin.ModelAdmin):
    list_display=('product_img','product_title','product_category')

class imageadmin(admin.ModelAdmin):
    list_display=('icon_image',)
 
admin.site.register(members,vegiAdmin)
 
admin.site.register(productdetails, products)

admin.site.register(imagedeatails,imageadmin)

