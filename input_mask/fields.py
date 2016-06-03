from django.conf import settings
from django import forms

from .utils import money_mask


class DecimalField(forms.DecimalField):
    def __init__(self, max_digits=10, decimal_places=2, *args, **kwargs):
        mask = kwargs.pop('mask', {})
        self.widget = money_mask(forms.TextInput, mask=mask)

        super(DecimalField, self).__init__(*args, **kwargs)

        self.widget.max_digits = max_digits
        self.widget.decimal_places = decimal_places

        self.localize = True

    def to_python(self, value):
        old_settings = settings.USE_L10N, settings.USE_THOUSAND_SEPARATOR

        settings.USE_L10N = True
        settings.USE_THOUSAND_SEPARATOR = True

        result = super(DecimalField, self).to_python(value)

        # restore original values
        settings.USE_L10N, settings.USE_THOUSAND_SEPARATOR = old_settings

        return result


class MoneyField(DecimalField):
    pass
