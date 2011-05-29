from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from subscriptions.utils import send_subscription_email

from django.views.generic import CreateView


class SubscriptionCreateView(CreateView):
    form_class = SubscriptionForm
    model = Subscription

    def get_success_url(self):
        return reverse('subscription:success', args=[self.object.pk])

    def form_valid(self, form):
        response = super(SubscriptionCreateView, self).form_valid(form)
        # envia email
        send_subscription_email(self.object)
        # continua...
        return response


def success(request, id):
    subscription = get_object_or_404(Subscription, pk=id)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscriptions/success.html', context)
