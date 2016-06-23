"""
Set of unit tests for utility functions
"""
import unittest

from phantomas.utils import format_args, is_sequence


class UtilsTestClass(unittest.TestCase):
    """  Unit tests for utility functions """

    @staticmethod
    def test_is_sequence():
        """  Unit tests for is_sequence function """
        assert is_sequence([])
        assert is_sequence([1, 2, 3])
        assert is_sequence((1, 2, 3))

        assert not is_sequence({})
        assert not is_sequence({'foo': 'bar'})
        assert not is_sequence(123)
        assert not is_sequence('test')
        assert not is_sequence(None)

    @staticmethod
    def test_format_args():
        """  Unit tests for format_args function """
        assert format_args({}) == []
        assert format_args({'foo': 'bar'}) == ['--foo=bar']
        assert format_args({'check': True}) == ['--check']
        assert format_args({'no-check': True}) == ['--no-check']
        assert format_args({'no_check': True}) == ['--no-check']
        assert format_args({'list': ['foo', 'bar', 123]}) ==\
            ['--list=foo,bar,123']
