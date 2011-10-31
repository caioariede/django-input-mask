from mask_field.widgets import InputMask


class USPhoneNumberInput(InputMask):
    mask = '{mask:"999-999-9999"}'


class USSocialSecurityNumberInput(InputMask):
    mask = '{mask:"999-99-9999"}'


class BRZipCodeInput(InputMask):
    mask = '{mask:"99999-9999"}'
