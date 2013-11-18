from ....widgets import *


class BRPhoneNumberInput(InputMask):
    mask = {
        'mask': '(99) 999999999',
    }


class BRZipCodeInput(InputMask):
    mask = {
        'mask': '99999-999',
    }


class BRCPFInput(InputMask):
    mask = {
        'mask': '999.999.999-99',
    }


class BRCNPJInput(InputMask):
    mask = {
        'mask': '99.999.999/9999-99',
    }


class BRDecimalInput(DecimalInputMask):
    thousands_sep = '.'
    decimal_sep = ','
