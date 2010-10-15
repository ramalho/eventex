# coding: utf-8
from django.http import HttpResponse
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
    context = RequestContext(request, {'form': SubscriptionForm()})

    if request.method == 'POST':
        return render_to_response('subscription/success.html', context)

    return render_to_response('subscription/new.html', context)

