from django.shortcuts import render_to_response


def homepage(request):
    from django.conf import settings
    context = {'MEDIA_URL': settings.MEDIA_URL}

    return render_to_response('index.html', context)
