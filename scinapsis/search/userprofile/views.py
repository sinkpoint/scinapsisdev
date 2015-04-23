from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from userprofile.models import UserProfile


import logging

def _get_user_info(req):
    if req.user:
        return req.user
    else:
        return None

# Create your views here.
def index(request):
    
    user = _get_user_info(request)
    #profile, created = UserProfile.objects.get_or_create(user=user)
    #profile.middle_name = 'yoyoyo'
    #profile.save()
    context = {'user': user}
    return render(request, 'userprofile/index.html', context)

def profilepage(request):
    user = _get_user_info(request)
    if user is not None:
        context = {'user': user}
        return render(request, 'userprofile/profilepage.html', context)
    return HttpResponseRedirect('userprofile:index')
    


def update_profile(request):
    
    return HttpResponseRedirect('userprofile:profilepage')

