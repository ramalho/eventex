from django.test import TestCase
from django.core.urlresolvers import reverse

from subscription.forms import SubscriptionForm

class SubscriptionViewTest(TestCase):

    def test_shows_form_with_errors_after_post_with_no_data(self):
        response = self.client.post(reverse('subscription:subscribe'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'subscription/new.html')
        self.assertTrue(isinstance(response.context['form'], SubscriptionForm))
        self.assertTrue(response.context['form'].errors)

