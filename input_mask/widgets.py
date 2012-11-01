from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from .utils import chunks


__all__ = (
    'InputMask',
    'DecimalInputMask',
)


class InputMask(forms.TextInput):
    def render(self, name, value, attrs=None):
        if hasattr(self, 'mask'):
            class_ = mark_safe('mask %s' % (self.mask,))

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

    def __init__(self, max_digits=10, decimal_places=2, *args, **kwargs):
        super(DecimalInputMask, self).__init__(*args, **kwargs)

        self.mask['mask'] = '%s%s%s' % (
            '9' * decimal_places,
            self.decimal_sep,
            chunks('9' * (max_digits - decimal_places), 3, self.thousands_sep),
        )
