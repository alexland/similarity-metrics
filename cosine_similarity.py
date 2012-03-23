#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import numpy as NP
from scipy import linalg as LA


def cos_sim(a, b) :
	return NP.dot(a, b) / (LA.norm(a) * LA.norm(b))
