#!/usr/bin/python

import sys #for argv
from fractions import gcd #built-in python gcd. Probably faster than mine from the previous homework.
import string
if len(sys.argv) != 2:
	print "Usage: vigenereDec.py cipherFile"
	exit()

cipherFile = open(sys.argv[1])

cipher = ""
#lengths between repetitions
lengths = []

#functions

		

def findRepeatedLength(str, start):
	"""Take a string and the first spot the string was seen, and returns the distance between
	repetitions in cipher. Returns [] if no matches are found. Otherwise, the return is an
	array of lengths"""
	lens = []
	curSpot = start + len(str)
	while curSpot + len(str) <= len(cipher):
		if curSpot > start and cipher[curSpot:curSpot+len(str)] == str:
			print str + " matched"
			lens.append(curSpot - start)
			start = curSpot
		curSpot += 1
	return lens
	

def findRepeats(size):
	"""Look for repeats with repeated string of size size"""
	global lengths, cipher
	curSpot = 0
	while curSpot < len(cipher):
		lengths = lengths + findRepeatedLength(cipher[curSpot:curSpot+size], curSpot)
		
		curSpot += 1

def findKeyLength():
	"""Find the most likely key length from the array of lengths"""
	


def Decrypt(keySize):
	""" Decrypt the cipher text, assuming key is of length keySize"""
	#TODO: Implement
	pass
###main###

#read cipherFile into cipher, a string
for l in cipherFile:
	l = "".join(l.strip().split())
	for c in string.punctuation:
		l = l.replace(c, "")
	cipher += l
print cipher

size = 10
while size > 2:
	print "trying size", size
	findRepeats(size)
	size -= 1

lengths = list(set(lengths))

print lengths
findKeyLength()