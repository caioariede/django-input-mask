from django import forms

from input_mask.fields import DecimalField, MoneyField
from input_mask.widgets import InputMask
from input_mask.utils import mask


class PhoneNumberMask(InputMask):
    mask = {'mask': '999-999-9999', 'placeholder': 'XXX-XXX-XXXX'}


class SSNMask(InputMask):
    mask = {'mask': '999-99-9999'}


class MoneyField(MoneyField):
    def __init__(self, *args, **kwargs):
        mask = {
            'precision': 0,
            'allowZero': False,
            'prefix': '$',
            'affixesStay': True,
        }

        mask.update(kwargs.pop('mask', {}))

        super(MoneyField, self).__init__(mask=mask, *args, **kwargs)


class BasicForm(forms.Form):
    decimal_field = DecimalField(max_digits=10, decimal_places=2)
    money_field = MoneyField(mask={'precision': 2})
    phone_number = forms.CharField(widget=PhoneNumberMask)
    ssn = forms.CharField(widget=SSNMask)
    date = forms.CharField(
        widget=mask(forms.DateInput,
                    mask='99/99/9999',
                    attrs={
                        'placeholder': 'MM/DD/YYYY',
                    },
                    format='%m/%d/%Y'))
