# coding: utf-8
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response

from subscription.forms import SubscriptionForm


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
            send_subscription_email(subscription)
            return HttpResponseRedirect(reverse('subscription:success'))
    else:
        form = SubscriptionForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def send_subscription_email(subscription):
    # render_to_string
    message_template = loader.get_template('subscription/subscription_email.txt')
    context = Context({'subscription': subscription})
    message = message_template.render(context)

    send_mail(
        subject = u'Inscrição no EventeX',
        message = message,
        from_email = 'contato@eventex.com',
        recipient_list = [ subscription.email ],
    )
