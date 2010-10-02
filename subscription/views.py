# coding: utf-8
from django.http import HttpResponse


def new(request):
    return HttpResponse(u'<h1>Formulário de Inscrição')