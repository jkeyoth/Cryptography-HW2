#!/usr/bin/python

import sys #for argv
from fractions import gcd #built-in python gcd. Probably faster than mine from the previous homework.

if len(sys.argv) != 2:
	print "Usage: vigenereDec.py cipherFile"
	exit()

cipherFile = open(sys.argv[1])

cipher = ""
letterCount=0
halfway = 0
#lengths between repetitions
lengths = []

#functions
def buildStringSplice(start, le):
	"""Return a string from cipher of length le starting at start. The string will contain l characters,
	but is not a normal slice, because it skips over anything that isn't a letter."""
	cnt = 0
	cur = 0
	ret = ""
	while cnt < le:
		if ord(cipher[start+cur]) >= ord("a") and ord(cipher[start+cur]) <= ord("z"):
			ret += cipher[start+cur]
			cnt += 1
		cur += 1
	return ret
		

def findRepeatedLength(str, start):
	"""Take a string and the first spot the string was seen, and returns the distance between
	repetitions in cipher. Returns [] if no matches are found. Otherwise, the return is an
	array of lengths"""
	if start + len(str) >= len(cipher):
		return []
	curSpot = start + len(str)
	while curSpot + len(str) <= len(cipher):
		if curSpot > start and cipher[curSpot:curSpot+len(str)] == str:
			return [curSpot - start] + findRepeatedLength(str, curSpot)
		curSpot += 1
	return []
	

def findRepeats(size):
	"""Look for repeats with repeated string of size size"""
	global lengths, cipher
	curSpot = 0
	while curSpot < len(cipher):
		lengths = lengths + findRepeatedLength(cipher[curSpot:curSpot+size], curSpot)
		
		curSpot += 1

def findKeyLength():
	"""Find the most likely key length from the array of lengths"""
	#TODO: Implement
	runningGCD = gcd(lengths[0], lengths[1])
	for le in lengths:
		runningGCD = gcd(runningGCD, le)
	return runningGCD


def Decrypt(keySize):
	""" Decrypt the cipher text, assuming key is of length keySize"""
	#TODO: Implement
	pass
###main###

#read cipherFile into cipher, a string
for l in cipherFile:
	cipher += l.strip().lower()

#count number of encrypted letters in cipher. Ignore any non-letters.
for c in cipher:
	if ord(c) >= ord("a") and ord(c) <= ord("z"):
		letterCount += 1
		
halfway = letterCount / 2

size = halfway
while size > 2:
	findRepeats(size)
	size -= 1

lengths = list(set(lengths))

print lengths
