#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import numpy as NP
import scipy.linalg as LA


def pearson(a, b) :
	"""
		returns pearson coef, -1 <= pc <= 1
	"""
	a = NP.array(a, dtype=float)
	numer = NP.sum(a*b) - (NP.sum(a) * NP.sum(b)/a.size)
	denom = ( (NP.sum(a**2) - NP.sum(a)**2/a.size) * 
				(NP.sum(b**2) - NP.sum(b)**2/b.size) )**.5
	if denom == 0 : 
		return 0
	return numer/denom


