from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

# Create your views here.

from .forms import SignUpForm

def home(request):
    return render_to_response ("base.html", locals (), context_instance =RequestContext(request))

def privacy(request):
    return render_to_response ("privacy.html", locals (), context_instance =RequestContext(request))

def blog(request):
    return render_to_response ("blog.html", locals (), context_instance =RequestContext(request))

def contact(request):
    return render_to_response ("contact.html", locals (), context_instance =RequestContext(request))

def comingsoon(request):
        
    form = SignUpForm (request.POST or None)
    
    
    if form.is_valid():
        save_it = form.save (commit=False)
        save_it.save ()
        messages.success(request, 'Thank you for joining.')
        
    return render_to_response ("comingsoon.html", locals (), context_instance =RequestContext(request))