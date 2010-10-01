from django.test import TestCase

class IndexUrlTest(TestCase):
    def test_success_when_get_index_page(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')
