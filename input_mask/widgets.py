from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.formats import get_format

from json import dumps

from .utils import chunks


__all__ = (
    'InputMask',
    'DecimalInputMask',
)


class InputMask(forms.TextInput):
    def render(self, name, value, attrs=None):
        if hasattr(self, 'mask'):
            class_ = 'mask %s' % (dumps(self.mask),)
            class_ = class_.replace('"', '&quot;')
            class_ = mark_safe(class_)

            if attrs is None:
                attrs = {'class': class_}
            elif 'class' not in attrs:
                attrs['class'] = class_
            else:
                attrs['class'] += ' ' + class_

        return super(InputMask, self).render(name, value, attrs=attrs)

    class Media:
        js = (settings.STATIC_URL + 'js/jquery.metadata.js',
              settings.STATIC_URL + 'js/jquery.meio.mask.min.js',
              settings.STATIC_URL + 'js/text_input_mask.js',)


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

    def render(self, *args, **kwargs):
        self.mask['mask'] = '%s%s%s' % (
            '9' * self.decimal_places,
            self.decimal_sep,
            chunks(
                '9' * (self.max_digits - self.decimal_places), 3,
                self.thousands_sep),
        )

        return super(DecimalInputMask, self).render(*args, **kwargs)
