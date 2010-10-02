# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response

def new(request):
    return render_to_response('subscription/new.html')