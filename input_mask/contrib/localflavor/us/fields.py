from ....fields import DecimalField
from .widgets import USDecimalInput

from decimal import Decimal


class USDecimalField(DecimalField):
    widget = USDecimalInput

    def to_python(self, value):
        return Decimal(value)
