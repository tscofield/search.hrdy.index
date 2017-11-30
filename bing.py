#!/usr/bin/env python3

import sys

# build dictionary of words
# disctionaries in python are a method of storing information in arrays
# it is concidental that we are storing a latin dictionary in a python
# dictionary

words = {}

# fill in dictionary
words['aestate'] = 'in summer'
words['altera'] = 'a second'
words['dum'] = 'while'

print ('hello, welcome to search.hrdy.index')

# Loop forever
while (1):
    # Prompt user, the \n makes a blank lines
    print ('\n\nenter the first letter of the latin word below')
    search = input()

    # loop through each dictionary entry
    for word, definition in words.items():
        # check if the word starts with the character we are looking for
        if word.startswith(search):
            # output the word and definition
            print (word, definition)

# we should never get here the while loop will run forever
# if we do get here exit cleanly
sys.exit(0)


search = input ()
if search == ('a') or ('A'):    #search a
    print ('aestate - in summer')
    print ('altera  - a second')
    search = input ()
if search == ('b') or ('B'):    #search b
    print ('404  No Results')
    search = input ()
if search == ('c') or ('C'):    #search C
    print ('Cur  -  why')
    search = input ()
if search == ('d') or ('D '):   #search D
    print ('dum  -  while')
    search = input ()
if search == ('e') or ('E'):   #search E
    print ('ecce  -  look')
    print ('et  -  amd')
    print ('etiam  -  also')
    search = input ()
if search == ('f') or ('F'):    #search F
    print ('404')
    search = input ()
if search == ('g') or ('G'):   #search G
    print ('404')
    search = input ()
if search== ('H') or ('h'):    #search H
    print ('habitat  -  now')
    search = input ()
if search== ('i') or ('I'):       #search I
    print ('iam  -  now')
    search = input ()
if search== ('l') or ('L'):    #search L
    print ('laeta  -  happy')
    print ('legit  -  reads')
    search = input ()
if search== ('m') or ('M'):     #search M
    print ('404')
    search = input ()
if search== ('n') or ('N'):      #searcharkch N
    print ('nomine  -  name')
    search = input ()
if search == ('o') or ('O'):    #search o
    print ('404')
    search = input ()
if search== ('p') or ('P'):      #search P
    print ('puella  -  girl')
    search = input ()
if search== ('q') or ('Q'):      #search Q
    print ('quae  -  who')
    print ('quid facit  -  what is doing')
    print ('quis  -  who')
    print ('quod  -  because')
    search = input ()
if search== ('r') or ('R'):     #search R
    print ('404')
    search = input ()
if search == ('s') or ('S'):    #search S
    print ('scribit  -  writes')
    print ('sedet  -  sits')
    print ('sub arbore  -  under (the) tree')
    search = input ()
if search == ('u') or ('U'):    #search U
    print ('ubi  -  where')
    search = input ()
if search == ('v') or ('V'):      #search V
    print ('vicina  -  neighboring')
    print ('villa  -  country house')
    print ('villa  -  rustica')
    search = input ()
if search == ('j') or ('k') or ('w') or ('x') or ('y') or ('z'):
    print ('unavailible')
    search = input ()
