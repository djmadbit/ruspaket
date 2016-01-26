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

	def get_context_data(self,**kwargs):
		context=super(ItemsListView,self).get_context_data(**kwargs)
		category_id=self.kwargs['pk']
		context['category']=Category.objects.get(pk=category_id)
		return context

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

@csrf_exempt
def CreateOrderView(request):
	print(request.POST)
	name=request.POST.get('name')
	phone=request.POST.get('phone')
	page=request.POST.get('page')
	Order.objects.create(name=name,phone=phone,page=page)
	
	msg=u'Новая заявка на сайте.\nИмя - '+name+u'\nТелефон: '+phone+u'\nСтраница: '+page
	send_mail(u'Новая заявка', msg, settings.DEFAULT_FROM_EMAIL, settings.EMAIL_ADMINS, fail_silently=False)
	return HttpResponse('OK')
	