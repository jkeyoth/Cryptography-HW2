#!/usr/bin/python

import operator
import string
import sys #for argv

if len(sys.argv) != 2:
	print "Usage: vigenereDec.py cipherFile"
	exit()

cipherFile = open(sys.argv[1])

MIN_KEY_LENGTH = 3
MAX_KEY_LENGTH = 20

cipher = ""
#lengths between repetitions
lengths = dict()
keySize = 0


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

def factors(num):
	facts = []
	for i in xrange(2, num/2):
		if num % i == 0:
			facts.append(i)
			facts.append(num/i)
	facts = list(set(facts))
	facts.sort(reverse=True)
	return facts

def splitToCeasers():
	"""Split the cipher into columns sharing the same encrypting key letter"""
	cnt = 0;
	columns = [""] * keySize
	for c in cipher:
		columns[cnt%keySize] += c
		cnt += 1
	return columns

def Decrypt():
	""" Decipher the cipher text, assuming key is of length keySize"""
	#TODO: Implement
	columns = splitToCeasers()
	print columns
###main###

#read cipherFile into cipher, a string
origCipher=""
for l in cipherFile:
	origCipher += l
	l = "".join(l.strip().split())
	for c in string.punctuation:
		l = l.replace(c, "")
	cipher += l

MAX_KEY_LENGTH = len(cipher) / 10

findRepeats()

sortedLengths = sorted(lengths.iteritems(), key=operator.itemgetter(1))
sortedLengths.reverse()

keySize = sortedLengths[0][0]
print "Key length:",keySize

print factors(8192)
