#-*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

from subscription.forms import SubscriptionForm
from subscription.models import Subscription

class SubscriptionViewTest(TestCase):

    def test_shows_form_with_errors_when_post_with_no_data(self):
        response = self.client.post(reverse('subscription:subscribe'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'subscription/new.html')
        self.assertTrue(isinstance(response.context['form'], SubscriptionForm))
        self.assertTrue(response.context['form'].errors)

    def test_subscription_is_saved_on_successful_post(self):
        self.assertFalse(Subscription.objects.exists())
        response = self.client.post(reverse('subscription:subscribe'), {
            'name': 'Guido Van Rossum',
            'cpf': '11111111111',
            'email': 'bdfl@python.org',
            'phone': '+1 754 3020 2000'
        })
        self.assertRedirects(response, reverse('subscription:success', args=[1]))
        self.assertTrue(Subscription.objects.exists())

    def test_email_is_sent_after_saving_subscription(self):
        # Verifica se não existe nenhum e-mail a ser enviado
        self.assertEquals(len(mail.outbox), 0)

        response = self.client.post(reverse('subscription:subscribe'), {
            'name': 'Guido Van Rossum',
            'cpf': '11111111111',
            'email': 'bdfl@python.org',
            'phone': '+1 754 3020 2000'
        })
        self.assertRedirects(response, reverse('subscription:success', args=[1]))

        # Verifica se um e-mail entrou na fila para ser enviado depois
        # do nosso POST
        self.assertEquals(len(mail.outbox), 1)
