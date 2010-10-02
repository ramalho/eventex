from django.test import TestCase
from django.core.urlresolvers import reverse


class SubscriptionUrlTest(TestCase):
    def test_successful_get_subscription_page(self):
        response = self.client.get(reverse('subscription:new'))
        self.assertEquals(200, response.status_code)


