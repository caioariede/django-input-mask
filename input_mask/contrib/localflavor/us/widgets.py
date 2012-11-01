from ....widgets import *


class USPhoneNumberInput(InputMask):
    mask = {
        'mask': '999-999-9999',
    }


class USSocialSecurityNumberInput(InputMask):
    mask = {
        'mask': '999-99-9999',
    }


class USZipCodeInput(InputMask):
    mask = {
        'mask': '99999-9999',
    }


class USDecimalInput(DecimalInputMask):
    thousands_sep = ','
    decimal_sep = '.'
