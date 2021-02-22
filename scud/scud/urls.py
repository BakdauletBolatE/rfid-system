from django import urls
from django.contrib import admin
from django.http import JsonResponse
from django.http import Http404
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import get_list_or_404, get_object_or_404

from main.models import SessionsToUser,Users


def index(request):
    session = SessionsToUser.objects.latest('id')
    context = {
        'session':session
    }
    return render(request,'index.html',context)

def jsonLatest(request):
    session = list(SessionsToUser.objects.values())
    latest = SessionsToUser.objects.last()

    if latest.user_id:
        user = list(Users.objects.values().get(id=latest.user_id))
        
    
    return JsonResponse({'data':session,'user':user})

urlpatterns = [
    path('',index),
    path('getl/',jsonLatest),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
