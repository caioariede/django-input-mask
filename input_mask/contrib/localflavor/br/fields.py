from ....fields import DecimalField
from .widgets import BRDecimalInput

from decimal import Decimal


class BRDecimalField(DecimalField):
    widget = BRDecimalInput

    def to_python(self, value):
        value = value.replace(',', '.')
        value = value.replace('.', '', value.count('.')-1)

        return Decimal(value)
