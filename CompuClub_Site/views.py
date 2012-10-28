from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext

def home(request):
    return render_to_response('main/index.html', context_instance=RequestContext(request))
