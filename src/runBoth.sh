#!/bin/bash
python vigenereEnc.py key.txt plain.txt > cipher.txt
python vigenereDec.py cipher.txt
