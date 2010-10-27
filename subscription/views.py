# coding: utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscription.forms import SubscriptionForm
from subscription.models import Subscription


#def new(request):
#    context = RequestContext(request, {'form': SubscriptionForm()})
#    return render_to_response('subscription/new.html', context)
#
#def create(request):
#    form = SubscriptionForm(request,)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))
    else:
        form = SubscriptionForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
