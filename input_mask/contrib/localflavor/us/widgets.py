from input_mask.widgets import (
    InputMask,
    DecimalInputMask,
)


class USPhoneNumberInput(InputMask):
    mask = {
        'mask': '999-999-9999',
    }


class USSocialSecurityNumberInput(InputMask):
    mask = {
        'mask': '999-99-9999',
    }


class BRZipCodeInput(InputMask):
    mask = {
        'mask': '99999-9999',
    }


class USDecimalInput(DecimalInputMask):
    thousands_sep = ','
    decimal_sep = '.'
