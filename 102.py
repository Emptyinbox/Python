#!/bin/python3

#importing
def nl():
    print('\n')
nl()
print("Importing is important")

nl()
import sys #sytem functions and parameters
from datetime import datetime 
print(datetime.now())

from datetime import datetime as dt #import as an alias
print(dt.now())
nl()
print("Advanced Strings")
nl()
my_name = "James"
print(my_name[0])# first letter
print(my_name[-1])# last

sentence = "This is a sentence."

print(sentence[:4])#first word
print(sentence[-9:-1]) #last word

print(sentence.split())#split sentence by default delimiter (space)
sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)
print("\n".join(sentence_split))



