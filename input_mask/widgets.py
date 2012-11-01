from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


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
