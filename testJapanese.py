# -*- coding: utf-8 -*-

# Basic Python File to understand code interacts with other languages

import unicodedata
import sys
# 
# a = 'ぐ'
# e = 'げ'
# 
# print a
# 
# b = a.decode("utf-8")
# # print ord(b)
# 
# print unichr(ord(b)+2)

dictionaryForm = raw_input("Dictionary Form: ")
# print "Dictionary Form: " + dictionaryForm

masuForm = dictionaryForm.decode("utf-8")
stem_length = len(masuForm) - 2

masu = 'ます'

# Ru-Verbs
# print masuForm[:stem_length+1] + masu.decode("utf-8")

# U-Verbs
# utoe = unichr(ord(masuForm[stem_length+1])-1)
# print "Masu Form: " + masuForm[:stem_length+1] + utoe + masu.decode("utf-8")

# Irregular Verbs
if (masuForm == ('いく').decode("utf-8")):
	masuForm = ('行き').decode("utf-8")
	print masuForm + masu.decode("utf-8")
elif (masuForm == ('くる').decode("utf-8")):
	masuForm = ('来').decode("utf-8")
	print masuForm + masu.decode("utf-8")
else:
	print "Verb is neither"
	
# print masuForm + masu.decode("utf-8")