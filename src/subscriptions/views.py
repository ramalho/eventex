from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from subscriptions.utils import send_subscription_email


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', context)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscriptions/new.html', context)

    subscription = form.save()
    # notifica o cadastro
    send_subscription_email(subscription)
    return HttpResponseRedirect(reverse('subscriptions:success', args=[ subscription.pk ]))


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscriptions/success.html', context)
