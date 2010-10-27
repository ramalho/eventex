#-*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

from subscription.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ('paid', )

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()
    subscribed_today.short_description = _('Inscrito hoje?')
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%(count)d inscrição foi marcada como paga.',
            u'%(count)d inscrições foram marcadas como pagas.',
            count
        ) % {'count': count}
        self.message_user(request, msg)
    mark_as_paid.short_description = _(u"Marcar como pagas")


admin.site.register(Subscription, SubscriptionAdmin)
