"""
# Importa o model Subscription
>>> from subscription.models import Subscription


# Faz uma inscrição bem sucedida
>>> Subscription.objects.create(name='Henrique Bastos', cpf='05633165780', email='henrique@bastos.net', phone='21-9618-6180')
<Subscription: Subscription object>


# CPF deve ser único
>>> Subscription.objects.create(name='Henrique Bastos', cpf='05633165780', email='othermail@bastos.net', phone='21-9618-6180')
------------------------------------------------------------
Traceback (most recent call last):
...
IntegrityError: column cpf is not unique


# Email deve ser único
>>> Subscription.objects.create(name='Henrique Bastos', cpf='38067528772', email='henrique@bastos.net', phone='21-9618-6180')
------------------------------------------------------------
Traceback (most recent call last):
...
IntegrityError: column email is not unique

"""