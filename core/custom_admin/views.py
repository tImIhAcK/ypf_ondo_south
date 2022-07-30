from urllib import response
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib import messages

from core.mixins import(
    AjaxFormMixin,
    FormErrors,
    RedirectParams
)

from . forms import (
    LocationForm,
    ParticipantForm,
    ConvertForm
)    

# class LocationView(TemplateView):
#     """Generic FormView with our mixin to display location page

#     Args:
#         TemplateView (_type_): _description_
#     """
#     template_name = 'admin/location.html'
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    
@login_required()
def location(request):
    if request.method == "POST":
        form = LocationForm(data = request.POST)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, f'Location created sucessfully')
            return redirect('location')
            # result = "Success"
            # message = "Your location has been created"
        # else:
        #     form = LocationForm()
        # #     message = FormErrors(form)
        # # data = {'result': result, 'message': message}
        # # return JsonResponse(data)
    else:
        form = LocationForm()
    return render(request, 'admin/location.html', context={'form': form})
        
@login_required()
def participant(request):
    if request.method == "POST":
        form = ParticipantForm(data = request.POST)
        # form.program = 'Impact 2022 June Edition'
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, f'Participant registered sucessfully')
            return redirect('participant')
        else:
            messages.error(request, 'Error registering participant')
    else:
        form = ParticipantForm()
    return render(request, 'admin/participant.html', context={'form': form})
        
@login_required()
def convert(request):
    if request.method == "POST":
        form = ConvertForm(data = request.POST)
        # form.program = 'Impact 2022 June Edition'
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, f'Convert registered sucessfully')
            return redirect('convert')
        else:
            messages.error(request, 'Error registering convert')
    else:
        form = ConvertForm()
    return render(request, 'admin/convert.html', context={'form': form})

# class ParticipantView(TemplateView):
#     """Generic FormView with our mixin to display location page

#     Args:
#         TemplateView (_type_): _description_
#     """
#     template_name = 'admin/participant.html'
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    

# class ConvertView(TemplateView):
#     """Generic FormView with our mixin to display location page

#     Args:
#         TemplateView (_type_): _description_
#     """
#     template_name = 'admin/convert.html'
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)



# @login_required()
# def participant(request):
#     return render(request, 'admin/participant.html')

# @login_required()
# def convert(request):
#     return render(request, 'admin/convert.html')