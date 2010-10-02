# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response

from subscription.forms import SubscriptionForm


def new(request):
    context = {'form': SubscriptionForm()}
    return render_to_response('subscription/new.html', context)