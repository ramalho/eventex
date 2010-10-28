#-*- coding: utf-8 -*-
from django import forms
from subscription.models import Subscription
from django.utils.translation import ugettext_lazy as _
from subscription import validators


class SubscriptionForm(forms.Form):
    name = forms.CharField()
    cpf = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()


"""
# 1 - ModelForm

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')
"""