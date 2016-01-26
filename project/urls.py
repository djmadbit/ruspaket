from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from django.conf import settings


urlpatterns = [
	url(r'^tinymce/', include('tinymce.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'',include('store.urls')),
]


if settings.DEBUG:
	urlpatterns += [
		url(r'^static/(?P<path>.*)$', views.serve),
	]	
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	import debug_toolbar
	urlpatterns += patterns('',
		url(r'^__debug__/', include(debug_toolbar.urls)),
	)
