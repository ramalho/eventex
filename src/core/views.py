from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from django.views.generic import TemplateView
from django.views.generic import DetailView

from core.models import Talk, Speaker


class HomepageView(TemplateView):
    template_name = 'index.html'


class TalkListView(TemplateView):
    template_name = 'core/talks.html'

    def get_context_data(self, **kwargs):
        context = super(TalkListView, self).get_context_data(**kwargs)

        context['morning_talks'] = Talk.objects.at_morning()
        context['afternoon_talks'] = Talk.objects.at_afternoon()

        return context


class TalkDetailView(DetailView):
    model = Talk
    context_object_name = 'talk'


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker_detail.html', {'speaker': speaker})
