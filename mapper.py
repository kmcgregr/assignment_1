#!/usr/bin/env python
import sys


stop_words = ["a","about","about","above","after","again","against","all","am","an", \
              "and","any","are","aren't","as","at","be"]
e_book_dictionary = {}

#--- get all lines from stdin ---
for line in sys.stdin:

#--- remove leading and trailing whitespace---
    line=line.strip()
#--- split the line into words ---
    words=line.split()
    for word in words:
        if word not in stop_words:
            print ("%s\t%s" %(word,"1"))
            #--create dictionary for popular words filter
            if word in e_book_dictionary:
                e_book_dictionary[word] = e_book_dictionary[word] + 1
            else:
                e_book_dictionary[word] = 1

#--get the top 50 popular words
top_words = 0
while (top_words < 50):
    for word in sorted(e_book_dictionary, key = e_book_dictionary.get,reverse=True):
        if word.startswith('e') or word.endswith('e'):
            print ("%s\t%s" %(word, str(e_book_dictionary[word])))
            top_words = top_words + 1
            if top_words == 50:
                sys.exit()
 