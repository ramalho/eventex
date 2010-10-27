#-*- coding: utf-8 -*-
from django.test import TestCase
from subscription.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_if_form_has_no_paid_field(self):
        form =  SubscriptionForm()
        self.assertNotIn('paid', form.fields)

    def test_returns_error_with_less_than_11_digits_in_cpf(self):
        form = SubscriptionForm({
            'name': 'User',
            'cpf': '123456789',
            'email': 'user@gmail.com',
            'phone': '555-78376',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('cpf', form.errors)
