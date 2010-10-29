from django.shortcuts import render_to_response
from django.template import RequestContext

from core.models import Talk


def homepage(request):
    from django.conf import settings
    context = {'MEDIA_URL': settings.MEDIA_URL}

    return render_to_response('index.html', context)

def talks(request):
    context = RequestContext(request, {
        'morning_talks': Talk.morning.filter(),
        'afternoon_talks': Talk.afternoon.filter(),
    })
    return render_to_response('core/talks.html', context)
