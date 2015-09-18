from django.conf import settings
from django.forms import DecimalField

from .widgets import DecimalInputMask


class DecimalField(DecimalField):
    widget = DecimalInputMask

    def __init__(self, max_digits=10, decimal_places=2, *args, **kwargs):
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
