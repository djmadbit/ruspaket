from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.CategoriesView.as_view(),name='categories_list'),
	url(r'^category/(?P<slug>.+)/$', views.ItemsListView.as_view(),name='item_list'),
	url(r'^create_order/$',views.CreateOrderView,name='create_order'),
	url(r'^items/(?P<slug>.+)/$', views.ItemDetailView.as_view(),name='item_detail'),
]