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
    list_display = ('first_name', 'last_name', 'gender', 'email', 'phone_no')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination')
    
@admin.register(Convert)
class ConvertAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email', 'phone_no')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination')

# admin.site.unregister(Group)