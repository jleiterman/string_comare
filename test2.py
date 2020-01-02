import random
def get_hint(fullset,revealedset):
    seed_length = random.randrange(20,40)
    seed_start = random.choice(list(fullset-revealedset))
    if seed_start+seed_length > max(fullset):
        seed_length = max(fullset) - seed_start
    return revealedset.union(set(range(seed_start,seed_start+seed_length)))

def printrevealedstring(shortstring,fullset,revealedset):
    printstring = ''
    for i in fullset:
        if i in revealedset:
            printstring = printstring+shortstring[i]
        else:
            printstring = printstring+'*'
    print(printstring)

import difflib

def evaluateinputstring(inputstring,shortstring,fullset,revealedset):
    s = difflib.SequenceMatcher(None, inputstring, shortstring, autojunk=False)
    blocks = s.get_matching_blocks()
    matchedstring = shortstring[blocks[0][1]:blocks[-2][1]+blocks[-2][2]]
    s2= difflib.SequenceMatcher(None, inputstring, matchedstring, autojunk=False)
    print("match Ratio:" +str(s2.ratio()))
    if s2.ratio() > .9:
        print("Input string:   "+inputstring)
        print("Matched string: "+matchedstring)
        #revealedset = revealedset | set(range(blocks[0][1],blocks[-2][1]+blocks[-2][2]))
        return revealedset.union(set(range(blocks[0][1],blocks[-2][1]+blocks[-2][2])))
    else:
        print("no match try again")
        return revealedset

import os
import string  

os.system('clear')
with open('longstring', 'r') as file:
#    data = file.read().replace('\n', '')
    longstring = file.read()
stringsplit = longstring.split("\n")
continue_var = True

while continue_var:
    shortstring = random.choice(stringsplit)
    fullset = set(range(0,len(shortstring)-1))
    revealedset = set()
    for i in fullset:
        if shortstring[i] == ' ' or shortstring[i] in string.punctuation:
            revealedset = revealedset.union(set([i]))
    printrevealedstring(shortstring, fullset,revealedset)
    while fullset != revealedset:
        inputstring = input("fill in the blanks: ") 
        os.system('clear')
        if inputstring == '':
            revealedset = get_hint(fullset,revealedset)
        else:
            revealedset = evaluateinputstring(inputstring,shortstring,fullset,revealedset)
        printrevealedstring(shortstring, fullset,revealedset)
    #continueinuput = input("Want to continue (y/n): ")
    if input("Want to continue (y/n): ") == 'n':
        continue_var = False
    os.system('clear')
      

    
