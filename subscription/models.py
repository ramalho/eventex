from django.db import models
from subscription.receivers import send_subscription_email

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

models.signals.post_save.connect(send_subscription_email, sender=Subscription)
