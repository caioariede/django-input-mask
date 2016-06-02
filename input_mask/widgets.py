from django import forms

from .utils import mask_cls, money_mask_cls


__all__ = (
    'InputMask',
    'DecimalInputMask',
)


InputMask = mask_cls(forms.TextInput)


class DecimalInputMask(money_mask_cls(forms.TextInput)):
    mask = {
        'thousands': '',
        'allowNegative': True,
    }
