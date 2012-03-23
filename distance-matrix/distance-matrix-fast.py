#!/usr/local/bin/python2.7
# encoding: utf-8

import sys
import os
import numpy as NP


def calcDistanceMatrixFastEuclidean3(nDimPoints) :
	nDimPoints = array(nDimPoints)
	n, m = nDimPoints.shape
	data = nDimPoints[:,0]
	delta = (data - data[:,newaxis])**2
	for d in xrange(1,m):
		data = nDimPoints[:,d]
		delta += (data - data[:,newaxis])**2
	return sqrt(delta)
