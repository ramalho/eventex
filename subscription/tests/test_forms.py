#-*- coding: utf-8 -*-
from django.test import TestCase
from subscription.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_if_form_has_no_paid_field(self):
        form =  SubscriptionForm()
        self.assertFalse(form.fields.get('paid'))
        #self.assertNotIn('paid', form.fields)

    def test_returns_error_with_less_than_11_digits_in_cpf(self):
        form = SubscriptionForm({
            'name': 'User',
            'cpf': '123456789',
            'email': 'user@gmail.com',
            'phone': '555-78376',
        })
        self.assertFalse(form.is_valid())
        #self.assertIn('cpf', form.errors)
        self.assertTrue(form.errors.get('cpf'))

    def test_returns_error_if_cpf_is_not_all_digits(self):
        form = SubscriptionForm({
            'name': 'User',
            'cpf': '0123456789a',
            'email': 'user@gmail.com',
            'phone': '555-78376',
        })
        self.assertFalse(form.is_valid())
        #self.assertIn('cpf', form.errors)
        self.assertTrue(form.errors.get('cpf'))

    def test_must_inform_email_or_phone(self):
        form = SubscriptionForm({
            'name': 'User',
            'cpf': '01234567891',
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.get('__all__'))