from django.conf import settings

import json


def encode_options(opts):
    return json.dumps(opts).replace('"', '&quot;')


def mask_cls(widget_cls):
    class InputMask(widget_cls):
        mask = {}

        def __init__(self, **kwargs):
            mask = kwargs.pop('mask', {})

            if type(mask) != object:
                mask = {'mask': mask}

            super(InputMask, self).__init__(**kwargs)

            self.mask.update(mask)

        def render(self, name, value, attrs=None):
            attrs = attrs or {}
            attrs['data-input-mask'] = encode_options(self.mask)
            return super(InputMask, self).render(name, value, attrs=attrs)

        class Media:
            js = (
                settings.STATIC_URL + 'input_mask/js/jquery.maskedinput.min.js',  # noqa
                settings.STATIC_URL + 'input_mask/js/text_input_mask.js',
            )

    return InputMask


def mask(widget_cls, **kwargs):
    return mask_cls(widget_cls)(**kwargs)


def money_mask_cls(widget_cls):
    class MoneyMask(widget_cls):
        mask = {
            'allowZero': True,
        }

        def __init__(self, **kwargs):
            mask = kwargs.pop('mask', {})

            super(MoneyMask, self).__init__(**kwargs)

            self.mask.update(mask)

        def render(self, name, value, attrs=None):
            attrs = attrs or {}
            attrs['data-money-mask'] = encode_options(self.mask)
            return super(MoneyMask, self).render(name, value, attrs=attrs)

        class Media:
            js = (
                settings.STATIC_URL + 'input_mask/js/jquery.maskMoney.min.js',
                settings.STATIC_URL + 'input_mask/js/text_input_mask.js',
            )

    return MoneyMask


def money_mask(widget_cls, **kwargs):
    return money_mask_cls(widget_cls)(**kwargs)


def decimal_mask(widget_cls, **kwargs):
    mask = {
        'thousands': '',
        'allowNegative': True,
    }

    override_mask = kwargs.pop('mask', {})
    mask.update(override_mask)

    return money_mask_cls(widget_cls)(mask=mask, **kwargs)
