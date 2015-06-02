Python module for easy integration with `phantomas <https://github.com/macbre/phantomas>`__ - PhantomJS-based modular web performance metrics collector

.. image:: https://pypip.in/version/phantomas/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/phantomas/
    :alt: Latest Version
.. image:: https://pypip.in/download/phantomas/badge.svg?period=week&style=flat
    :target: https://pypi.python.org/pypi/phantomas/
    :alt: Latest Version
.. image:: https://pypip.in/py_versions/phantomas/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/phantomas/
    :alt: Supported Python versions
.. image:: https://travis-ci.org/macbre/phantomas-python.svg?branch=master
    :target: https://travis-ci.org/macbre/phantomas-python

Install
-------

In order to use this module you need `phantomas` "binary" installed in your system.

::

    sudo make install

This will run `npm install -g phantomas`.

Module's API
------------

::

    import json
    from phantomas import Phantomas
    
    results = Phantomas(
        url="http://example.com",
        exec_path="/my/path/to/phantomas",     # optional
        modules=['headers', 'requestsStats']
    ).run()

    print('Generator: ' + results.get_generator())   # phantomas v1.9.0
    print('\nMetrics: ' + json.dumps(results.get_metrics(), indent=True, sort_keys=True))
    print('\nDomains: ' + json.dumps(results.get_offenders('domains'), indent=True))

    # assertions
    assert results.get_metric('notFound') == 0
    assert results.get_metric('requests') < 5

More docs coming soon! Meanwhile please refer to `example/example.py` script.
