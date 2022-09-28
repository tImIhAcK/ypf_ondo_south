from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

app_name = 'custom_admin'
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)