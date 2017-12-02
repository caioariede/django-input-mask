from django import forms

from .utils import input_mask, decimal_mask


__all__ = (
    'InputMask',
    'DecimalInputMask',
)


InputMask = input_mask(forms.TextInput)

class DecimalInputMask(decimal_mask(forms.TextInput)):
    pass
