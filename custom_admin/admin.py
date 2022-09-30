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
    
# def move_to_convert(modeladmin, request, queryset):
#     filtered_participant = queryset.values_list('first_name', 'last_name', 'gender', 'age', 'phone_no',
#                                        'email', 'linkedin', 'address', 'city', 'state', 'region',
#                                        'category', 'school', 'denomination').distinct() 
#     # convert = [Convert(**participant) for participant in filtered_participant]
#     print(filtered_participant)
#     # Convert.objects.bulk_create(convert)
# move_to_convert.short_description = "Move selected to convert"    

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')
    # actions = [move_to_convert, ]
    
@admin.register(Convert)
class ConvertAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')

# admin.site.unregister(Group)