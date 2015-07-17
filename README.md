Django Input Mask
=================

A collection of easy-to-extend-widgets for applying masks to input elements.

**License:** MIT

Status
------

[![Build Status](https://travis-ci.org/caioariede/django-input-mask.svg?branch=master)](https://travis-ci.org/caioariede/django-input-mask)

Compatibility
-------------

* Django 1.7 and 1.8
* Python 2.7 and 3.x

Requirements
------------

* jQuery 1.8 or higher

We do not include jQuery in this package, you must add it by your hands.

**Note:**
*jQuery 1.9 support will be granted through the* `jQuery Migrate Plugin <https://github.com/jquery/jquery-migrate>`_.

*Just take a look on* `example_project/templates/form.html <example_project/example_project/templates/form.html>`_ *file for an example.*

Installation
---

```bash
pip install django-input-mask
```

Configuration
---

Add ``input_mask`` to the ``INSTALLED_APPS`` setting.

*This is needed so that Django can handle the app's static files*

Usage
---

```python
from django import forms
from django.contrib.localflavor.br.forms import BRPhoneNumberField

from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput

class YourForm(forms.ModelForm):
     phone = BRPhoneNumberField(widget=BRPhoneNumberInput)
```

**Decimal masks**

```python
from input_mask.fields import DecimalField

class MyForm(forms.ModelForm):
    my_decimal_field = DecimalField(max_digits=10, decimal_places=2)
```
* `input_mask.fields.DecimalField` will automatically handle separators.
* `input_mask.contrib.localflavor.*.fields.*DecimalField` will use local-based separators.

**Creating your own masks**

```python
from input_mask.widgets import InputMask

class MyCustomInput(InputMask):
    mask = {'mask': '999-111'}
```

For more rules, take a look at `meioMask documentation <http://www.meiocodigo.com/projects/meiomask/>`_.
