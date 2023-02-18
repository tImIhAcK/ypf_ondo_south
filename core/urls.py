from django.contrib import admin
from django.urls import path, include
from custom_admin import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    # path('location/', views.location, name='location'),
    path('participant/', views.participant, name='participant'),
    path('convert/', views.convert, name='convert'),
    path('newcomer/', views.convert, name='newcomer'),
    
    
    
    path(r'', include('home.urls', namespace='home'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    