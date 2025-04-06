from unittest import TestCase

from app.src.core.utils.payload_utils import optional, required


class TestRequired(TestCase):
    def test_required_with_valid_key(self):
        obj = {"key": "value"}
        result = required(obj, "key")
        self.assertEqual(result, "value")

    def test_required_with_missing_key(self):
        obj = {}
        with self.assertRaises(ValueError):
            required(obj, "key", message="Key is missing")

    def test_required_with_null_value(self):
        obj = {"key": None}
        with self.assertRaises(ValueError):
            required(obj, "key", message="Key cannot be null")

    def test_required_with_custom_message(self):
        obj = {}
        with self.assertRaises(ValueError) as context:
            required(obj, "key", message="Custom error message")
        self.assertEqual(str(context.exception), "Custom error message")

    def test_required_with_default_value(self):
        obj = {}
        result = required(obj, "key", default="default_value")
        self.assertEqual(result, "default_value")

    def test_required_with_default_value_and_valid_key(self):
        obj = {"key": "value"}
        result = required(obj, "key", default="default_value")
        self.assertEqual(result, "value")


class TestOptional(TestCase):
    def test_optional_with_valid_key(self):
        obj = {"key": "value"}
        result = optional(obj, "key")
        self.assertEqual(result, "value")

    def test_optional_with_missing_key(self):
        obj = {}
        result = optional(obj, "key", default="default_value")
        self.assertEqual(result, "default_value")

    def test_optional_with_null_value(self):
        obj = {"key": None}
        result = optional(obj, "key", default="default_value")
        self.assertEqual(result, "default_value")

    def test_optional_without_default_value(self):
        obj = {}
        result = optional(obj, "key")
        self.assertIsNone(result)
