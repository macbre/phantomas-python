#!/usr/bin/env python
"""
Run phantomas several times against http://example.com and display the results
"""
import json
import logging

from phantomas import Phantomas, PhantomasError

logging.basicConfig(level=logging.DEBUG)

test = Phantomas(
    url="http://example.com",
    runs=3,
    modules=[
        'domains',
        'headers',
        'requestsStats',
        'timeToFirst'
    ]
)

try:
    runs = test.run()
    results = runs.runs[0]

    print(test)

    print(runs)
    print('Runs:      {0}'.format(len(runs.runs)))

    print('\nStats:')
    print(json.dumps(runs.stats, indent=True))

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
