from django.test import TestCase
from django.core.urlresolvers import reverse

from subscriptions.forms import SubscriptionForm


class SubscriptionUrlTest(TestCase):
    def test_successful_get_subscription_page(self):
        response = self.client.get(reverse('subscriptions:subscribe'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'subscriptions/subscription_form.html')

    def test_redirects_to_success_after_valid_post(self):
        response = self.client.post(reverse('subscriptions:subscribe'), {
            'name': 'Guido Van Rossum',
            'cpf': '11111111111',
            'email': 'bdfl@python.org',
            'phone': '+1 754 3020 2000'
        })
        self.assertRedirects(response, reverse('subscriptions:success', args=[1]))

