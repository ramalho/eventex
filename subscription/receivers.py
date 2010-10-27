#-*- coding: utf-8 -*-
from django.template import Context, loader
from django.core.mail import send_mail

def send_subscription_email(sender, **kwargs):
    subscription = kwargs.get('instance')

    if subscription is None:
        raise ValueError('This function must be connected to: post_save of Subscription')

    # render_to_string
    message_template = loader.get_template('subscription/subscription_email.txt')
    context = Context({'subscription': subscription})
    message = message_template.render(context)

    send_mail(
        subject = u'Inscrição no EventeX',
        message = message,
        from_email = 'contato@eventex.com',
        recipient_list = [ subscription.email ],
    )
