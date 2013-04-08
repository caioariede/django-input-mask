from django import forms

from input_mask.fields import DecimalField


class BasicForm(forms.Form):
    decimal_field = DecimalField(max_digits=10, decimal_places=2)
