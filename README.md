**Django Input Mask**

A collection of widgets for applying masks to input elements using JavaScript.

**Requirements**

* jQuery 1.2.6+

Note: _We do not include jQuery in this package, you must add it by your hands._

**Installation**

`pip install git+http://github.com/codasus/django-input-mask#egg=input_mask`

Or manually place it on your `PYTHON_PATH`.

**Usage**

    from django import forms
    from django.contrib.localflavor.br.forms import BRPhoneNumberField

    from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput


    class YourForm(forms.ModelForm):
        phone = BRPhoneNumberField(widget=BRPhoneNumberInput)

**Creating your own masks**

    from input_mask.widgets import InputMask

    
    class MyCustomInput(InputMask):
        mask = '{mask: "999-111"}'


For more rules, take a look at [meioMask documentation](http://www.meiocodigo.com/projects/meiomask/).

**License**

Django Input Mask by [Codasus Technologies](http://codasus.com) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

You are free:

* to Share - to copy, distribute and transmit the work
* to Remix - to adapt the work
* to make commercial use of the work
