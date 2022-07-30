from django.contrib import admin
from .models import Location, Participant, Convert

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'district', 'region')
    
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email', 'phone_no', 'school', 'profession')
    
@admin.register(Convert)
class ConvertAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email', 'phone_no')