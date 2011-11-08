from django.test import TestCase
from django.core.urlresolvers import reverse

from subscription.forms import SubscriptionForm


class SubscriptionUrlTest(TestCase):
    def test_successful_get_subscription_page(self):
        response = self.client.get(reverse('subscription:subscribe'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'subscription/new.html')

    def test_redirects_to_success_after_valid_post(self):
        response = self.client.post(reverse('subscription:subscribe'), {
            'name': 'Guido Van Rossum',
            'cpf': '11111111111',
            'email': 'bdfl@python.org',
            'phone_0': '754',
            'phone_1': '30202000',
        })
        self.assertRedirects(response, reverse('subscription:success', args=[1]))

