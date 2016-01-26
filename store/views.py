# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.core.mail import send_mail
from django.conf import settings 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse

from .models import Item,Category,Order

class CategoriesView(ListView):
	model=Category
	template_name="category_list.html"
	context_object_name="categories"

class ItemsListView(ListView):
	model=Item
	template_name="item_list.html"
	context_object_name="items"
	slug_field = 'utm'

	def get_context_data(self,**kwargs):
		context=super(ItemsListView,self).get_context_data(**kwargs)
		category_utm=self.kwargs['slug']
		context['category']=Category.objects.get(utm=category_utm)
		return context

	def get_queryset(self):
		utm=self.kwargs['slug']
		return Item.objects.filter(category__utm=utm).select_related()	

class ItemDetailView(DetailView):
	model=Item
	context_object_name='item'
	template_name='item.html'
	slug_field = 'utm'

	def get_context_data(self,**kwargs):
		context=super(ItemDetailView,self).get_context_data(**kwargs)
		item=self.get_object()
		context['like_items']=Item.objects.exclude(id=item.id).filter(category=item.category)
		return context

@csrf_exempt
def CreateOrderView(request):
	try:
		name=request.POST.get('name')
		phone=request.POST.get('phone')
		page=request.POST.get('page')
		desc=request.POST.get('desc')

		Order.objects.create(name=name,phone=phone,page=page,desc=desc)
		
		msg=u'Новая заявка на сайте.\nИмя: '+name+u'\nТелефон: '+phone+u'\n'+desc
		send_mail(u'Новая заявка', msg, settings.DEFAULT_FROM_EMAIL, settings.EMAIL_ADMINS, fail_silently=False)
		return JsonResponse({'status':'success'})
	except:
		return JsonResponse({'status':'fail'}) 	