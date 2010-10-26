from django.test import TestCase
from subscription.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_if_form_has_no_paid_field(self):
        form =  SubscriptionForm()
        self.assertNotIn('paid', form.fields)
