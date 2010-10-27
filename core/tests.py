from django.test import TestCase
from django.core.urlresolvers import reverse


class HomepageUrlTest(TestCase):
    def test_success_when_get_homepage(self):
        response = self.client.get(reverse('homepage'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')
