from django.contrib import admin
from django.urls import path, include
from custom_admin import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('location/', views.location, name='location'),
    path('participant/', views.participant, name='participant'),
    # path('participant', views.ParticipantView.as_view(), name='participant'),
    path('convert/', views.convert, name='convert'),
    # path(r'get_groups_data/', views.get_groups_data, name='get_groups_data'),
    # path(r'get_districts_data/', views.get_districts_data, name='get_districts_data'),
    
    
    
    path(r'', include('home.urls', namespace='home'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    