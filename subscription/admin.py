from django.contrib import admin

from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at')

    date_hierarchy = 'created_at'

admin.site.register(Subscription, SubscriptionAdmin)
