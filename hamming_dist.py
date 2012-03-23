#!/usr/local/bin/python2.7
# encoding: utf-8

import sys
import os


def hamming_dist(s1, s2):
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


