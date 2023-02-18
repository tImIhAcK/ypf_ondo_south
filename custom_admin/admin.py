from django.contrib import admin
from .models import Participant, Convert, Region, State, Newcomer
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display= ('id', 'region', 'state')
    list_filter=('state',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state')
    
def move_to_convert(modeladmin, request, queryset):
    for participant in queryset:
        convert = Convert.objects.create(
            first_name=participant.first_name,
            last_name=participant.last_name,
            gender=participant.gender,
            age=participant.age,
            phone_no=participant.phone_no,
            email=participant.email,
            linkedin=participant.linkedin,
            address=participant.address,
            city=participant.city,
            state=participant.state,
            region=participant.region,
            category=participant.category,
            school=participant.school,
            denomination=participant.denomination
        )
        convert.save()
        messages.success(request, f"{len(queryset)} converts moved to convert.")


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')
    actions = [move_to_convert, ]
    
    def move_to_convert(self, obj):
        return mark_safe('<a class="button" href="{}">Move the convert</a>',
                           reverse('admin:move-participant-to-convert') + f"?ids={obj.id}")
    move_to_convert.short_description = "Move selected to convert"    
    
@admin.register(Convert)
class ConvertAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')

@admin.register(Newcomer)
class NewcomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'region', 'state')
    list_filter = ('gender', 'state', 'region', 'category', 'denomination', 'registered_date')
# admin.site.unregister(Group)