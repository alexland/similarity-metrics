#!/usr/local/bin/python2.7
# encoding: utf-8


import numpy as NP


def jaccard(vec1, vec2) :
    """
        returns Jaccard Index for 2 bit-wise vectors;
        pass in 2 x NumPy 1D arrays (type is int/float/boolean, if former 2,
        values of 0, 1 only ) of *equal* size.
    """
    vec1, vec2 = NP.squeeze(vec1), NP.squeeze(vec2)
    fnx = lambda v : NP.array(v, dtype=bool)
    vec1, vec2 = fnx(vec1), fnx(vec2)
    try :
        numer = NP.sum(vec1 == vec2)
    except ValueError :
        print("check that the 2 vectors are of equal length")
    denom = float(vec1.size)
    return numer / denom


def similarity(uid):
	vec1 = r0.get(uid)
	all_vecs = [ [r0.get(k), k] for k in r0.keys('*')]
	jaccard_scores = sorted([ [jaccard(vec1, vec), k for vec in all_vecs ])[1:]


def tanimoto(A, B) :
	"""
	returns Tanimoto coefficient;
	A & B is A *union* B (!= intersection)

	"""
	A, B = set(A), set(B)
	numer = len(A & B)
	denom = len(A) + len(B) - len(A & B)
	return numer/float(denom)


def tanimoto_bool(A, B) :
	"""
		returns Tanimoto coefficient;
		accepts two 1D vectors, comprised of 1s & 0s
	"""
	AuB = NP.sum(A==B)
	numer = AuB
	denom = len(A) + len(B) - AuB
	return numer/float(denom)



headers = ['sex', 'acquisition_channel', 'forum_participation_level',
			'account_type']


input_fields = ['male', 'female',
				'new', 'trusted', 'active_participant', 'moderator',
				'direct_typein', 'organic_search', 'affiliate',
				'premium_subscriber', 'regular_subscriber', 'unregistered_user']


>>> row1 = NP.array([0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0])

>>> row2 = NP.array([1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0])

>>> row1.dtype
  dtype('int64')
>>> row1.itemsize
  8

>>> row1 = NP.array(row1, dtype=bool)
>>> row2 = NP.array(row2, dtype=bool)
>>> row1.dtype
  dtype('bool')
>>> row1.itemsize
  1

# calculate a pair-wise similarity score (row1 & row2)
>>> row1 == row2  # element-wise comparison
   array([False, False, False, False,  True,  True, False,  True,  True, False],
			dtype=bool)
>>> NP.sum(row1==row2)
  5


def tanimoto_bool(A, B) :
	AuB = NP.sum(A==B)
	numer = AuB
	denom = len(A) + len(B) - AuB
	return numer/float(denom)


