# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from tinymce.models import HTMLField

class Category(models.Model):
	title=models.CharField(
		verbose_name=u'Название',
		max_length=255,
	)
	utm=models.CharField(
		verbose_name=u'UTM метка',
		max_length=255,
	)
	price_from=models.IntegerField(
		verbose_name=u'Цена от',
		default=0,
	)
	price_to=models.IntegerField(
		verbose_name=u'Цена до',
		default=0,
	)
	min_count=models.IntegerField(
		verbose_name=u'Минимальное количество',
		default=0,
	)
	full_about=HTMLField(
		verbose_name=u'Полное описание',
		default='',
		blank=True,
	)
	short_about=HTMLField(
		verbose_name=u'Краткое описание',
		default='',
		blank=True,
	)
	image=models.ImageField(
		verbose_name=u'Изображение',
	)

	def __str__(self):
		return (self.title).encode('utf-8')

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
	utm=models.CharField(
		verbose_name=u'UTM метка',
		max_length=255,
	)
	price_from=models.IntegerField(
		verbose_name=u'Цена от',
		default=0,
	)
	price_to=models.IntegerField(
		verbose_name=u'Цена до',
		default=0,
	)
	min_count=models.IntegerField(
		verbose_name=u'Минимальное количество',
		default=0,
	)
	full_about=HTMLField(
		verbose_name=u'Полное описание',
		default='',
		blank=True,
	)
	short_about=HTMLField(
		verbose_name=u'Краткое описание',
		default='',
		blank=True,
	)
	image=models.ImageField(
		verbose_name=u'Изображение',
	)

	def __str__(self):
		return (self.title).encode('utf-8')

	class Meta:
		verbose_name=u'Товар'
		verbose_name_plural=u'Товары'

class Order(models.Model):
	item=models.ForeignKey(
		Item,
		verbose_name=u'Товар',
	)
	name=models.CharField(
		verbose_name=u'ИМЯ',
		max_length=1024,
	)
	phone=models.CharField(
		verbose_name=u'Телефон',
		max_length=255,
	)

	def __str__(self):
		return (self.name+' '+self.phone).encode('utf-8')

	class Meta:
		verbose_name=u'Заявка'
		verbose_name_plural=u'Заявки'