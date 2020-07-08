from django.shortcuts import render, redirect
from django.http import HttpResponse
from rec.models import Notifications
from django.template import loader

# Create your views here.

def index(request):
    
    notifications = Notifications.objects.all().order_by('-timestamp')[:3]

    

    template = loader.get_template('rec/index.html')
    
    context = {
        'notifications':notifications,
        
    }
    
    
    return HttpResponse(template.render(context, request))