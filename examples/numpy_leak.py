#!/usr/bin/env python
# coding: utf-8

# see https://github.com/numpy/numpy/issues/7860

import numpy as np

# while True:
#     names = ['field{}'.format(i) for i in range(200)]
#     print len(names)
#     dt = np.dtype({"name": names, "formats": 200 * [np.uint8]})
#
#     arr = np.zeros((1000, ), dt)
#     sortedIndices = np.argsort(arr, order='field0')


n = 0
while True:
    names = ["POH"] + \
        ["Head %d Really Long Data Field Name With Many Words" % i for i in xrange(200)]
    formats = [">f"] + [">I"] * 200
    offsets = range(0, 804, 4)

    dt = np.dtype({"names": names, "formats": formats, "offsets": offsets})
    array = np.zeros((1000,), dt)

    sortedIndices = np.argsort(array, order=["POH"])