from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from core.models import Talk, Speaker


def homepage(request):
    from django.conf import settings
    context = {
        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render_to_response('index.html', context)

def talks(request):
    context = RequestContext(request, {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    })
    return render_to_response('core/talks.html', context)

def talk_detail(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    return direct_to_template(request, 'core/talk_detail.html', {
        'talk': talk,
        'slides': talk.media_set.filter(type="SL"),
        'videos': talk.media_set.filter(type="YT"),
    })


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker_detail.html', {'speaker': speaker})
