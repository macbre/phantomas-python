"""
Set of unit tests for Results class
"""
import unittest

from phantomas.results import Results


class ResultsTestClass(unittest.TestCase):
    """  Unit tests for Results class """
    URL = 'http://foo.bar.net/'

    def setUp(self):
        self.instance = Results(url=self.URL, data={
            'generator': 'foo v1.2.3',
            'metrics': {
                'request': 1,
                'notFound': 0,
            },
            'offenders': {
                'request': [
                    self.URL
                ]
            }
        })

    def test_get_metrics(self):
        """ Test get_metrics """
        assert self.instance.get_metrics() == {
            'request': 1,
            'notFound': 0,
        }

    def test_get_metric(self):
        """ Test get_metric """
        assert self.instance.get_metric('request') == 1
        assert self.instance.get_metric('notFound') == 0
        assert self.instance.get_metric('foo') is None
        assert self.instance.get_metric('foo', 0) == 0

    def test_get_offenders(self):
        """ Test get_offenders """
        assert self.instance.get_offenders('request') == [self.URL]
        assert self.instance.get_offenders('notFound') is None
        assert self.instance.get_offenders('foo') is None

    def test_get_url(self):
        """ Test get_url """
        assert self.instance.get_url() == self.URL

    def test_get_generator(self):
        """ Test get_generator """
        assert self.instance.get_generator() == 'foo v1.2.3'

    def test_repr(self):
        """ Test __repr__ helper """
        assert str(self.instance) == \
            '<Results for {url} (2 metrics)>'.format(url=self.URL)
