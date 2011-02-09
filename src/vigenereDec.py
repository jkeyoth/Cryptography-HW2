#!/usr/bin/python

import sys #for argv
from fractions import gcd #built-in python gcd. Probably faster than mine from the previous homework.
import string
if len(sys.argv) != 2:
	print "Usage: vigenereDec.py cipherFile"
	exit()

cipherFile = open(sys.argv[1])

MIN_KEY_LENGTH = 3
MAX_KEY_LENGTH = 20

cipher = ""
#lengths between repetitions
lengths = dict()
for i in xrange(MAX_KEY_LENGTH):
	lengths[i] = 0

#functions
def modShift(ammount):
	return cipher[ammount:len(cipher)] + cipher[0:ammount]

def findRepeats():
	for i in xrange(MIN_KEY_LENGTH, MAX_KEY_LENGTH):
		shifted = modShift(i)
		matches = 0
		for j in xrange(len(cipher)):
			if cipher[j] == shifted[j]:
				matches = matches + 1
		lengths[i] = matches
	

def findKeyLength():
	"""Find the most likely key length from the array of lengths"""
	

def Decrypt(keySize):
	""" Decrypt the cipher text, assuming key is of length keySize"""
	#TODO: Implement
	pass
###main###

#read cipherFile into cipher, a string
origCipher=""
for l in cipherFile:
	origCipher += l
	l = "".join(l.strip().split())
	for c in string.punctuation:
		l = l.replace(c, "")
	cipher += l
print cipher

findRepeats()

import operator
sortedLengths = sorted(lengths.iteritems(), key=operator.itemgetter(1))
sortedLengths.reverse()

print "(shift, occurrences)"
print sortedLengths[0]

findKeyLength()