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
#--- remove the stop words and add the remaining words to a dictionary---
    for word in words:
        if word not in stop_words:
            if word in e_book_dictionary:
                e_book_dictionary[word] = e_book_dictionary[word] + 1
            else:
                e_book_dictionary[word] = 1


for top_words in range(0,50):

    for word in sorted(e_book_dictionary, key = e_book_dictionary.get,reverse=True):
        if word.startswith('e') or word.endswith('e'):
            print (word, e_book_dictionary[word])
            top_words = top_words + 1
    #---print the top 50 words that begins with or ends with 'e'
    #for top_words in range(0,50):
    #for word in sorted(e_book_dictionary, key = e_book_dictionary.get,reverse=True):
     #   print (word, e_book_dictionary[word])
    #        if word.startswith('e') or word.endswith('e'):
     #           print (word,e_book_dictionary[word])
     #           top_words = top_words + 1