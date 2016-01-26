from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Item,Category,Order

class CategoriesView(ListView):
	model=Category
	template_name="category_list.html"
	context_object_name="categories"

class ItemsListView(ListView):
	model=Item
	template_name="item_list.html"
	context_object_name="items"

	def get_queryset(self):
		category=self.kwargs['pk']
		return Item.objects.filter(category_id=category)	

class ItemDetailView(DetailView):
	model=Item
	context_object_name='item'
	template_name='item.html'

	def get_context_data(self,**kwargs):
		context=super(ItemDetailView,self).get_context_data(**kwargs)
		item=self.get_object()
		context['like_items']=Item.objects.exclude(id=item.id).filter(category=item.category)
		return context

def CreateOrderView(request,utm):
	name=request.POST.get('name')
	phone=request.POST.get('phone')
	item=Item.objects.get(umt=utm)
	Order.objects.create(name=name,phone=phone,item=item)
	