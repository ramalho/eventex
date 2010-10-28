from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from subscription.utils import send_subscription_email


def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    s = Subscription()
    s.name = form.cleaned_data['name']
    s.cpf = form.cleaned_data['cpf']
    s.email = form.cleaned_data['email']
    s.phone = form.cleaned_data['phone']
    s.save()

    # notifica o cadastro
    send_subscription_email(s)
    return HttpResponseRedirect(reverse('subscription:success', args=[ s.pk ]))


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
