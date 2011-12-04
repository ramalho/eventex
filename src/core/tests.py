from django_testtools import TestCase
from django.core.urlresolvers import reverse


class HomepageUrlTest(TestCase):
    def test_success_when_get_homepage(self):
        response = self.client.get(reverse('homepage'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')


class PalestrasTest(TestCase):
    fixtures = ['talks.json']

    def assertPage(self, url, template=None):
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)

        if template:
            self.assertTemplateUsed(response, template)

    def test_show_palestras(self):
        self.assertPage('core:talks', 'core/talks.html')

    def test_show_palestra_detail(self):
        self.assertPage(reverse('core:talk_detail', args=[2]), 'core/talk_detail.html')

    def test_show_speaker_detail(self):
        self.assertPage(reverse('core:speaker', args=['henrique-bastos']), 'core/speaker.html')