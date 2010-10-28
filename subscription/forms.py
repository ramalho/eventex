#-*- coding: utf-8 -*-
from django import forms
from subscription.models import Subscription
from django.utils.translation import ugettext_lazy as _
from subscription import validators


class SubscriptionForm(forms.Form):
    name = forms.CharField(label=_('Nome'))
    cpf = forms.CharField(label=_('CPF'))
    email = forms.EmailField(label=_('E-mail'))
    phone = forms.CharField(required=False, label=_('Telefone'))


"""
#2 - Form básico feito na mão
class SubscriptionForm(forms.Form):
    name = forms.CharField()
    cpf = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()

# 1 - ModelForm

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')
"""