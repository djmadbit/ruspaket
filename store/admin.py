from django.contrib import admin

from .models import Category,Item,Order

class CategoryAdmin(admin.ModelAdmin):
	list_display=['title','price','min_count']
	prepopulated_fields = {'utm': ('title',)}

class ItemAdmin(admin.ModelAdmin):
	list_display=['title','utm','price','min_count','category']
	prepopulated_fields = {'utm': ('title',)}

class OrderAdmin(admin.ModelAdmin):
	list_display=['name','phone','desc','date_created']
	ordering=['-date_created']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Order,OrderAdmin)

