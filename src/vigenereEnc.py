#!/usr/bin/python

import sys #for argv

if len(sys.argv) != 3:
	print "Usage: vigenereEnc.py keyFile plainFile"
	exit()

def encryptLetter(l, key, keyPos):
	plainLetterNum = ord(l) - ord("a")
	keyNum = ord(key[keyPos]) - ord("a")
	cypherLetter = chr(((plainLetterNum + keyNum) % 26) + ord("a"))
	#print "key", key.rstrip(), "keyPos", keyPos, "plainLetterNum", plainLetterNum,
	#print "keyNum", keyNum, "cypherLetter", cypherLetter
	return cypherLetter
	


keyFile = None
plainFile = None

cypher = ""

try:
	keyFile = open(sys.argv[1])
except:
	print "keyFile open failed."

try:
	plainFile = open(sys.argv[2])
except:
	print "plainFile open failed."


key = keyFile.readline()
keyFile.close()

keyPos = 0

plain = []

for line in plainFile:
	for w in line:
		if ord(w.lower()) >= ord("a") and ord(w.lower()) <= ord("z"):
			cypherLetter = encryptLetter(w.lower(), key, keyPos)
			cypher += cypherLetter
			keyPos += 1
	
			if keyPos >= len(key):
				keyPos = 0
		else:
			cypher += w

print cypher.rstrip()
