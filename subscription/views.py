from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from subscription.utils import send_subscription_email


from django.views.generic import CreateView
from django.views.generic import DetailView


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


class SubscriptionSuccessView(DetailView):
    template_name = 'subscription/success.html'
    model = Subscription
