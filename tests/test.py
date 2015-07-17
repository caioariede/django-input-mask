from django.test import TestCase

from decimal import Decimal
from tests.forms import Form1


class InputMaskTest(TestCase):
    def test_decimal_field(self):
        data = {
            'dec_field': '1.98',
        }

        form = Form1(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('dec_field'), Decimal('1.98'))
