"""
Set of unit tests for Phantomas runner
"""
import os
import unittest

from phantomas.client import Phantomas
from phantomas.errors import PhantomasRunError, PhantomasResponseParsingError


class PhantomasRunTestClass(unittest.TestCase):
    """  Unit tests for Phantomas run class """
    URL = 'http://foo.bar.net/'

    def setUp(self):
        self._instance = Phantomas(url=self.URL)

    def test_run_os_error(self):
        """ Test failed execution of the binary """
        self._instance._cmd = 'foobar123'

        self.assertRaises(PhantomasRunError, self._instance.run)

    def test_run_json_parsing_failed(self):
        """ Test failed parsing of JSON """
        if os.path.isfile('/usr/bin/true'):
            self._instance._cmd = '/usr/bin/true'
        else:
            self._instance._cmd = '/bin/true'

        self.assertRaises(PhantomasResponseParsingError, self._instance.run)
