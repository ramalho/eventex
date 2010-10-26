#-*- coding: utf-8 -*-
from django.contrib import admin

from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'paid')

    date_hierarchy = 'created_at'

    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')

    list_filter = ('paid', )

    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        subscriptions_updated = queryset.update(paid=True)
        if subscriptions_updated == 1:
            msg = '%d inscrição foi marcada como paga' % subscriptions_updated
        else:
            msg = '%d inscrições foram marcadas como pagas' % subscriptions_updated
        self.message_user(request, msg)

    mark_as_paid.short_description = u"Marcar inscrições como pagas"

admin.site.register(Subscription, SubscriptionAdmin)
