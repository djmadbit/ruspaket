from django.contrib import admin

from .models import Category,Item,Order

class CategoryAdmin(admin.ModelAdmin):
	list_display=['title','price_from','price_to','min_count']

class ItemAdmin(admin.ModelAdmin):
	list_display=['title','utm','price_from','price_to','min_count','category']

class OrderAdmin(admin.ModelAdmin):
	list_display=['name','phone','desc','date_created']
	ordering=['-date_created']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Order,OrderAdmin)

