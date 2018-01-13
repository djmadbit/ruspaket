# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

from tinymce.models import HTMLField

class Category(models.Model):
	title=models.CharField(
		verbose_name=u'Название',
		max_length=255,
	)
	utm=models.SlugField(
		verbose_name=u'UTM метка',
		max_length=255,
		unique=True,
	)
	price=models.FloatField(
		verbose_name=u'Цена',
		default=0,
		blank=True,
		null=True,
	)
	min_count=models.CharField(
		verbose_name=u'Минимальное количество',
		default='',
		max_length=255,
		blank=True,
	)
	min_order=models.CharField(
		verbose_name=u'Минимальный заказ',
		default='',
		max_length=255,
		blank=True,
	)
	short_about=HTMLField(
		verbose_name=u'Краткое описание',
		default='',
		blank=True,
	)
	full_about=HTMLField(
		verbose_name=u'Полное описание',
		default='',
		blank=True,
	)
	image=models.ImageField(
		verbose_name=u'Изображение',
	)
	meta_keywords=models.TextField(
    	verbose_name=u'META keywords',
    	blank=True,
    	default='',
	)
	meta_description=models.TextField(
    	verbose_name=u'META description',
    	blank=True,
    	default='',
	)

	def __str__(self):
		return (self.title).encode('utf-8')

	@models.permalink
	def get_absolute_url(self):
		return ('item_list', (), {'slug': self.utm})

	class Meta:
		verbose_name=u'Категория'
		verbose_name_plural=u'Категории'

class Item(models.Model):
	category=models.ForeignKey(
		Category,
		verbose_name=u'Категория',
	)
	title=models.CharField(
		verbose_name=u'Название',
		max_length=255,
	)
	utm=models.SlugField(
		verbose_name=u'UTM метка',
		max_length=255,
		unique=True,
	)
	price=models.FloatField(
		verbose_name=u'Цена',
		default=0,
		blank=True,
		null=True,
	)
	min_count=models.CharField(
		verbose_name=u'Минимальное количество',
		default='',
		max_length=255,
		blank=True,
	)
	min_order=models.CharField(
		verbose_name=u'Минимальный заказ',
		default='',
		max_length=255,
		blank=True,
	)
	short_about=HTMLField(
		verbose_name=u'Краткое описание',
		default='',
		blank=True,
	)
	full_about=HTMLField(
		verbose_name=u'Полное описание',
		default='',
		blank=True,
	)
	image=models.ImageField(
		verbose_name=u'Изображение',
	)
	meta_keywords=models.TextField(
    	verbose_name=u'META keywords',
    	blank=True,
    	default='',
	)
	meta_description=models.TextField(
    	verbose_name=u'META description',
    	blank=True,
    	default='',
	)

	def __str__(self):
		return (self.title).encode('utf-8')

	@models.permalink
	def get_absolute_url(self):
		return ('item_detail', (), {'slug': self.utm})

	class Meta:
		verbose_name=u'Товар'
		verbose_name_plural=u'Товары'

class Order(models.Model):
	page=models.CharField(
		verbose_name=u'Страница',
		max_length=1024,
	)
	desc=models.CharField(
		verbose_name=u'Описание страницы',
		max_length=1024,
	)
	name=models.CharField(
		verbose_name=u'ИМЯ',
		max_length=1024,
		blank=True,
	)
	phone=models.CharField(
		verbose_name=u'Телефон',
		max_length=255,
	)
	date_created=models.DateTimeField(
		verbose_name=u'Дата создания',
		auto_now_add=True,
	)

	def __str__(self):
		return (self.name+' '+self.phone).encode('utf-8')

	class Meta:
		verbose_name=u'Заявка'
		verbose_name_plural=u'Заявки'