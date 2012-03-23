#!/usr/local/bin/python2.7
# encoding: utf-8

import numpy as NP

NP.set_printoptions(precision=3, suppress=True)

x = NP.random.randint(0, 10, 7).reshape(1, 7)
y = NP.random.randint(0, 10, 7).reshape(1, 7)

delx = x - x.T
dely = y - y.T

tx = delx**2
ty = dely**2

DM = NP.sqrt(tx + ty)

# replace '0' values along main diagonal with large values so 'argmin' 
# is not confused

v = 100 + NP.diag(DM)
T = NP.diag(v)
DM += T

def dist_matrix(x, y) :
	x = x.reshape(1, x.shape[0])
	y = y.reshape(1, y.shape[0])
	delx2 = (x - x.T)**2
	dely2 = (y - y.T)**2
	DM = NP.sqrt(delx2 + dely2)
	v = 999 + NP.diag(DM)
	T = NP.diag(v)
	DM += T
	return DM


x = NP.random.randint(0, 10, 15)
y = NP.random.randint(0, 10, 15)

DM = dist_matrix(x, y)

print(DM)

