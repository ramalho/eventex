#-*- coding: utf-8 -*-
from django import forms

from subscription.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')

    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        if len(data) != 11:
            raise forms.ValidationError('O CPF deve ter 11 dígitos')
        return data
