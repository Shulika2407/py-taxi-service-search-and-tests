from taxi.forms import DriverCreationForm
from django.test import TestCase


class FormTest(TestCase):
    def test_driver_create(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test First",
            "last_name": "Test Last",
            "license_number": "DFG15923",
        }
        form = DriverCreationForm(data=form_data)

        self.assertTrue(form.is_valid())

        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(form.cleaned_data["first_name"], form_data["first_name"])
        self.assertEqual(form.cleaned_data["last_name"], form_data["last_name"])
        self.assertEqual(form.cleaned_data["license_number"], form_data["license_number"])
