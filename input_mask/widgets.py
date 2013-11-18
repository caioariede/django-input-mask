from django import forms
from django.conf import settings
from django.utils import numberformat
from django.utils.safestring import mark_safe
from django.utils.formats import get_format

from json import dumps
from decimal import Decimal

from .utils import chunks


__all__ = (
    'InputMask',
    'DecimalInputMask',
)


class InputMask(forms.TextInput):
    def __init__(self, *args, **kwargs):
        mask = kwargs.pop('mask', {})
        super(InputMask, self).__init__(*args, **kwargs)
        self.mask.update(mask)

    def render(self, name, value, attrs=None):
        if hasattr(self, 'mask'):
            if self.mask.get('type') != 'reverse':
                class_ = 'mask '
            else:
                class_ = 'mask mask-reverse '

            class_ += dumps(self.mask).replace('"', '&quot;')

            if attrs is not None and 'class' in attrs:
                class_ = '%s %s' % (attrs['class'], class_)

            attrs['class'] = mark_safe(class_)

        return super(InputMask, self).render(name, value, attrs=attrs)

    class Media:
        js = (
            settings.STATIC_URL + 'input_mask/js/jquery.metadata.js',
            settings.STATIC_URL + 'input_mask/js/jquery.meio.mask.min.js',
            settings.STATIC_URL + 'input_mask/js/jquery19support.js',
            settings.STATIC_URL + 'input_mask/js/text_input_mask.js',
        )


class DecimalInputMask(InputMask):
    mask = {
        'type': 'reverse',
        'defaultValue': '000',
    }

    thousands_sep = get_format('THOUSAND_SEPARATOR')
    decimal_sep = get_format('DECIMAL_SEPARATOR')

    def __init__(self, max_digits=10, decimal_places=2, *args, **kwargs):
        super(DecimalInputMask, self).__init__(*args, **kwargs)

        self.max_digits = max_digits
        self.decimal_places = decimal_places

    def render(self, name, value, attrs=None):
        self.mask['mask'] = '%s%s%s' % (
            '9' * self.decimal_places,
            self.decimal_sep,
            chunks(
                '9' * (self.max_digits - self.decimal_places), 3,
                self.thousands_sep),
        )

        try:
            Decimal(value)
        except:
            pass
        else:
            value = numberformat.format(
                value,
                self.decimal_sep,
                decimal_pos=self.decimal_places,
                thousand_sep=self.thousands_sep,
            )

        return super(DecimalInputMask, self).render(name, value, attrs=attrs)
