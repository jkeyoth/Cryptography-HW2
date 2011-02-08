#!/usr/bin/python

import sys #for argv

if len(sys.argv) != 2:
	print "Usage: vigenereDec.py cipherFile"
	exit()

cipherFile = open(sys.argv[1])

cipher = ""
letterCount=0

#functions
def findIfRepeated(str):
	"""Take a string str and return the distance between repeations in cipher"""
	#TODO: Implement
	pass

def findRepeats(size):
	"""Look for repeats with repeated string of size size"""
	curSpot = 0;
	
def Decrypt(keySize):
	
	#TODO: Implement

###main###

#read cipherFile into cipher, a string
for l in cipherFile:
	cipher += l.strip()

#count number of encrypted letters in cipher. Ignore any non-letters.
for c in cipher:
	if ord(c.lower()) >= ord("a") and ord(c.lower()) <= ord("z"):
		letterCount += 1

print letterCount
