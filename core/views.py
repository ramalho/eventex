from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from core.models import Talk, Speaker


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

def talk_details(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    slides = talk.media_set.filter(type="SL")
    videos = talk.media_set.filter(type="YT")
    context = RequestContext(request, {
        'talk': talk,
        'slides': slides,
        'videos': videos,
    })
    return render_to_response('core/talk.html', context)

def speaker(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = RequestContext(request, {
        'speaker': speaker,
    })
    return render_to_response('core/speaker.html', context)
