#-*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_subscription_email(subscription):
    if subscription is None:
        raise ValueError('This function must be connected to: post_save of Subscription')

    subject = u'Inscrição no EventeX realizada com sucesso.'
    message = render_to_string(
        'subscription/email.txt',
        {'subscription': subscription }
    )

    send_mail(
        subject = subject,
        message = message,
        from_email = settings.DEFAULT_FROM_EMAIL,
        recipient_list = [ subscription.email ],
    )
