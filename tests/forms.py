from django import forms

from input_mask.fields import DecimalField


class Form1(forms.Form):
    dec_field = DecimalField(max_digits=10, decimal_places=2)
