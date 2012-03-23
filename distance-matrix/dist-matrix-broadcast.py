#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import numpy as NP

# a simple vector quantization (given a set of data vectors, find the nearest neighbor for each from among a set of 'prototype arrays' given a calculations)

>>> # make up some data
>>> # first, the protype arrays
>>> C = NP.random.randint(0, 10, 15).reshape(5, 3)
>>> # then the data points
>>> D = NP.random.randint(0, 10, 30).reshape(10, 3)
>>> C.shape
(5, 3)
>>> D.shape
(10, 3)

# probably the most conceptually straightforward technique for vector quantization is creation of a distance matrix--i.e., an array storing the pairwise distances for every data point and every prototype vector. So, we start by calculating the Euclidean distance. In pseudococe: [(x2-x1)^2 + (y2-y1)^2]^0.5

>>> diff = D[NP.newaxis,:,:] - C[:,NP.newaxis,:]
>>> diff.shape
(5, 10, 3)
>>> DM = NP.sqrt(NP.sum(diff**2, axis=1))
>>> DM.shape
(5, 3)

# There is an excellent discussion n the NumPy docs of the exact issue recited in the OP.

# As you know, the answer depends on size of the array created from the broadcast operation, but soem generalization is possible:

# (i) consider the size of the array created from the broadcast operation relative to the size of the precursor arrays; and

# (ii) even for simple computation, as you increase the size of the data set, the point at which looping beats broadcasting performance-wise, is reached very quickly; and

# (iii) the question is usually not whether to use broadcasting or not, but which steps of the computation to broadcsat.

# The NumPy docs report a measured time of 2.245 seconds for broadcasting and 1.637 for the looping alternative (in this case, that is 2D broadcasting followed by looping over the data array)





http://www.scipy.org/EricsBroadcastingDoc