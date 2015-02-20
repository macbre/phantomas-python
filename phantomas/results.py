"""
phantomas results wrapper
"""


class Results(object):
    """ Phantomas results wrapper """

    def __init__(self, url, data):
        for key in ['generator', 'metrics', 'offenders']:
            assert data.get(key) is not None

        self._url = url

        self._generator = data.get('generator')
        self._metrics = data.get('metrics')
        self._offenders = data.get('offenders')

    def get_metric(self, name, default=None):
        """ Get metric value """
        return self._metrics.get(name, default)

    def get_metrics(self):
        """ Get all metrics as key/value dict """
        return self._metrics

    def get_offenders(self, name):
        """ Get offenders for a given metric """
        return self._offenders.get(name)

    def get_url(self):
        """ Get URL of the pages phantomas has been run for """
        return self._url

    def get_generator(self):
        """ Get results generator - phantomas vX.Y.Z """
        return self._generator

    def __repr__(self):
        return '<Results for {url} ({count} metrics)>'.format(
            url=self._url,
            count=len(self._metrics)
        )


class Runs(object):
    """ Phantomas runs wrapper """

    def __init__(self, url, data):
        for key in ["runs", "stats"]:
            assert data.get(key) is not None

        self._url = url
        self._runs = [Results(url=self.url, data=run_data) for run_data in data["runs"]]
        self._stats = data.get("stats")

    @property
    def url(self):
        return self._url

    @property
    def stats(self):
        return self._stats

    @property
    def runs(self):
        return self._runs or []


