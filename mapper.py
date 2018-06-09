#!/usr/bin/env python
import sys

#--- get all lines from stdin ---
stop_words = ["a","about","about","above","after","again","against","all","am","an", \
              "and","any","are","aren't","as","at","be"]
e_book_dictionary = {}

for line in sys.stdin:

#--- remove leading and trailing whitespace---
    line=line.strip()
#--- split the line into words ---
    words=line.split()
#--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        if word not in stop_words:
            if word in e_book_dictionary:
                e_book_dictionary[word] = e_book_dictionary[word] + 1
            else:
                e_book_dictionary[word] = 1
            print ("%s\t%s" %(word,"1"))
