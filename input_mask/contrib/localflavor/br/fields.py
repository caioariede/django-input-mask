from django.forms import ValidationError

from ....fields import DecimalField
from .widgets import BRDecimalInput

from decimal import Decimal, DecimalException


class BRDecimalField(DecimalField):
    widget = BRDecimalInput

    def to_python(self, value):
        value = value.replace(',', '.')
        value = value.replace('.', '', value.count('.') - 1)

        try:
            value = Decimal(value)
        except DecimalException:
            raise ValidationError(self.error_messages['invalid'])
