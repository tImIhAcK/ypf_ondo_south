from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
# from django.conf.urls import url

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.download, name='download')
    # url(r'^download/(?<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)