**Django Input Mask**

A collection of easy-to-extend-widgets for applying masks to input elements.

**Requirements**

* jQuery 1.2.6+

Note: _We do not include jQuery in this package, you must add it by your hands._

**Installation**

`pip install git+http://github.com/codasus/django-input-mask.git#egg=input_mask`

Or manually place it on your `PYTHON_PATH`.

**Configuration**

Add 'input_mask' to your `INSTALLED_APPS`.

*This is needed so that Django can handle the app's static files*

**Usage**

    from django import forms
    from django.contrib.localflavor.br.forms import BRPhoneNumberField

    from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput


    class YourForm(forms.ModelForm):
        phone = BRPhoneNumberField(widget=BRPhoneNumberInput)

**Creating your own masks**

    from input_mask.widgets import InputMask

    
    class MyCustomInput(InputMask):
        mask = {
            'mask': '999-111',
        }

**Decimal masks**

    from input_mask.fields import DecimalField

    class MyForm(forms.ModelForm):
        my_decimal_field = DecimalField(max_digits=10, decimal_places=2)

* input_mask.fields.DecimalField will automatically handle separators.
* input_mask.contrib.localflavor.*.fields.*DecimalField will use local-based separators.

For more rules, take a look at [meioMask documentation](http://www.meiocodigo.com/projects/meiomask/).

**MIT License**

<pre>Copyright (c) 2011 Caio Ariede and Codasus Technologies.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.</pre>
