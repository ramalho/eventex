# encoding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from subscription.models import Subscription


class SubscriptionModelTest(TestCase):
    def test_create_new_subscription(self):
        s = Subscription.objects.create(
            name='Henrique Bastos',
            cpf='05633165780',
            email='henrique@bastos.net',
            phone='21-9618-6180'
        )
        self.assertEquals(s.id, 1)


class SubscriptionModelUniqueTest(TestCase):
    fixtures = ['subscription.json']

    def test_cpf_must_be_unique(self):
        s = Subscription(
            name='Henrique Bastos',
            cpf='05633165780',
            email='henrique@bastos.net',
            phone='21-9618-6180'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_must_be_unique(self):
        s = Subscription(
            name='Henrique Bastos',
            cpf='38067528772',
            email='henrique@bastos.net',
            phone='21-9618-6180')
        self.assertRaises(IntegrityError, s.save)