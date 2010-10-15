# coding: utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from subscription.forms import SubscriptionForm


#def new(request):
#    context = RequestContext(request, {'form': SubscriptionForm()})
#    return render_to_response('subscription/new.html', context)
#
#def create(request):
#    form = SubscriptionForm(request,)

def subscribe(request):
    form = SubscriptionForm()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('subscription:success'))

    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

