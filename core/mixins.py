from email import message
from urllib.parse import urlencode
from django.conf import settings
from django.shortcuts import redirect
import requests
# import json
# import datetime
# from humanfriendly import ti
from django.http import JsonResponse
from django.contrib import messages


def FormErrors(**args):
    """Handles erros that are passed to AJAX call

    Returns:
        _type_: _message_
    """
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message

def RedirectParams(**kwargs):
    """Used to append URL when redirecting user
    """
    url = kwargs.get('url')
    params = kwargs.get('params')
    response = redirect(url)
    if params:
        query_string = urlencode(params)
        response['Location'] += '?' + query_string
        
    return response

class AjaxFormMixin(object):
    """Mixing Ajaxify django form

    Args:
        object (_type_): _description_
    """
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            message = FormErrors(form)
            return JsonResponse({'result':'Error', 'message':message})
        return response
    
    def form_valid(self, form, request):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            form.save()
            messages.success(request, "Sucessfull")
            # return JsonResponse({'result':'Sucess', 'message':""})
        return response
            
