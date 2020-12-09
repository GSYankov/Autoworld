from django.forms import ModelForm
from orders.models import Offer


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['price']
