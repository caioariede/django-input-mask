from django.forms import DecimalField

from .widgets import DecimalInputMask


class DecimalField(DecimalField):
    widget = DecimalInputMask

    def __init__(self, max_digits=10, decimal_places=2, *args, **kwargs):
        super(DecimalField, self).__init__(*args, **kwargs)

        self.widget.max_digits = max_digits
        self.widget.decimal_places = decimal_places
