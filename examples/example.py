#!/usr/bin/env python
"""
Run phantomas against http://example.com and display the results
"""
import logging

from phantomas import Phantomas

logging.basicConfig(level=logging.DEBUG)

test = Phantomas(
    url="http://example.com",
    modules=[
        'headers',
        'requestsStats',
        'timeToFirst'
    ]
)

results = test.run()

print(test)
print(results)
