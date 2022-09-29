from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Participant, Convert, Region, State

# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display= ('id', 'region', 'state')
    list_filter=('state',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state')
    


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')
    
@admin.register(Convert)
class ConvertAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')

# admin.site.unregister(Group)