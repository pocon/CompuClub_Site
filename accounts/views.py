from fixtures.models import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required

def logout(request):
    logout(request)
    return redirect('/')
    
def register(request):
    return redirect('/')

# Login is not needed!
