#!/usr/bin/env python
"""
Run phantomas against http://example.com and display the results
"""
import json
import logging

from phantomas import Phantomas, PhantomasError

logging.basicConfig(level=logging.DEBUG)

test = Phantomas(
    url="http://example.com",
    modules=[
        'domains',
        'headers',
        'requestsStats',
        'timeToFirst'
    ]
)

try:
    results = test.run()

    print(test)
    print(results)

    print('Generator: ' + results.get_generator())
    print('URL:       ' + results.get_url())

    print('\nMetrics:')
    print(json.dumps(results.get_metrics(), indent=True, sort_keys=True))

    print('\nDomains:')
    print(json.dumps(results.get_offenders('domains'), indent=True))

    # assertions
    assert results.get_metric('notFound') == 0
    assert results.get_metric('requests') < 5

except AssertionError as ex:
    print('Assertion failed')
    exit(1)

except PhantomasError as ex:
    print(ex)
    exit(2)
