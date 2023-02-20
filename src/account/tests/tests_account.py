from django.core.exceptions import ValidationError
from django.test import TestCase

from core.utils.samples import sample_account


class TestAccountModel(TestCase):
    def setUp(self):
        self.test_account = sample_account(
            email="abc@gmail.com", password="12345", first_name="Mary", last_name="Jons"
        )
        self.test_account.get_short_name()
        self.test_account.get_full_name()

    def tearDown(self):
        self.test_account.delete()

    def test_first_name_max_length(self):
        with self.assertRaises(ValidationError):
            sample_account(email="abc@gmail.com", password="12345", first_name="A" * 1000)

    def test_last_name_max_length(self):
        with self.assertRaises(ValidationError):
            sample_account(email="abc@gmail.com", password="12345", last_name="A" * 1000)

    def test_get_short_name(self):
        self.assertEqual(self.test_account.get_short_name(), "Mary")

    def test_get_full_name(self):
        self.assertEqual(self.test_account.get_full_name(), "Mary Jons")
