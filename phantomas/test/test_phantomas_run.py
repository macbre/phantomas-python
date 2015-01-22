"""
Set of unit tests for Phantomas runner
"""
import unittest

from ..client import Phantomas
from ..errors import PhantomasRunError, PhantomasResponseParsingError


class PhantomasRunTestClass(unittest.TestCase):
    """  Unit tests for Phantomas run class """
    URL = 'http://foo.bar.net/'

    def setUp(self):
        self._instance = Phantomas(url=self.URL)

    def test_run_os_error(self):
        """ Test failed execution of the binary """
        self._instance.CMD = 'foobar123'

        self.assertRaises(PhantomasRunError, self._instance.run)

    def test_run_json_parsing_failed(self):
        """ Test failed parsing of JSON """
        self._instance.CMD = '/bin/true'

        self.assertRaises(PhantomasResponseParsingError, self._instance.run)
