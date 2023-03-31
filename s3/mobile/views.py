from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobile
# Create your views here.

def mobile(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobile/mobile.html', {'mobiles': mobiles})

def info(request, pk):
    mobile = Mobile.objects.get(id=pk)
    return render(request, 'mobile/info.html', {'mobile': mobile})