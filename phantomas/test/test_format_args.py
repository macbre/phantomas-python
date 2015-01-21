"""
Set of unit tests for helper functions
"""
import unittest

from ..client import Phantomas


class FormatArgsTestClass(unittest.TestCase):
    """  Unit tests for Phantomas class """

    def test_format_args(self):
        """  Unit tests for Phantomas.format_args method """
        self.assertEqual(Phantomas.format_args(dict()), [])
        self.assertEqual(Phantomas.format_args(dict(foo="bar")), ['--foo=bar'])
        self.assertEqual(Phantomas.format_args(dict(check=True)), ['--check'])
        self.assertEqual(Phantomas.format_args(
            dict(list=['foo', 'bar', 123])), ['--list=foo,bar,123'])
