Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
print(os.path.join('C:',os.sep, 'Documents'))
/Documents
fo = open("words.txt", "r+")
str = fo.readline()
import random
text_file = open("words.txt", "r")
lines = text_file.readlines()
for x in range(0,4):
    print(lines[random.randint(0,len(lines)-1)])

    
conserve

foisted

extractive

tossing

