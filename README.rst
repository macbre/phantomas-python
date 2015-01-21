Python module for easy integration with `phantomas <https://github.com/macbre/phantomas>`__

Install
-------

In order to use this module you need `phantomas` "binary" installed in your system.

::

    sudo make install

This will run node.js' `npm` that will install phantomas globally.

Module's API
------------

::

    import json
    from phantomas import Phantomas
    
    results = Phantomas(
        url="http://example.com",
        modules=['headers', 'requestsStats']
    ).run()
    
    print results.getMetric('requests')  # get the "requests" metric
    print json.dumps(results.getOffenders('requests'), indent=True)  # get offenders for the "requests" metric
