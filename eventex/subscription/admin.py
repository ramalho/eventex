#-*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse

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

    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_url = patterns('',
            # Envolvemos nossa view em 'admin_view' por que ela faz o
            # controle de permissões e cache automaticamente para nós.
            url(r'exportar-inscricoes/$', self.admin_site.admin_view(self.export_subscriptions), name='export_subscriptions')
        )
        # A ordem é importante. As URLs originais do admin são muito permissivas
        # e acabam sendo encontradas antes da nossa se elas estiverem na frente.
        return extra_url + original_urls

    def export_subscriptions(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions]

        response = HttpResponse('\r\n'.join(rows), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'

        return response

admin.site.register(Subscription, SubscriptionAdmin)
