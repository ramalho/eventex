from django_testtools import TestCase
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
from core.models import Talk


class HomepageUrlTest(TestCase):
    def test_success_when_get_homepage(self):
        response = self.client.get(reverse('core:homepage'))
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
        self.assertPage(reverse('core:speaker_detail', kwargs={'slug': 'henrique-bastos'}), 'core/speaker_detail.html')


class TalkProperties(TestCase):
    fixtures = ['talks.json']

    def test_slides_property(self):
        talk = Talk.objects.get(pk=2)
        self.assertIsInstance(talk.slides, QuerySet)
        self.assertTrue(talk.slides.exists())

    def test_videos_property(self):
        talk = Talk.objects.get(pk=2)
        self.assertIsInstance(talk.videos, QuerySet)
        self.assertTrue(talk.videos.exists())