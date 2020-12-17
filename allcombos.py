#BEGIN
import itertools
import os
import sys

def allcombos(alphabet, minlen=1, maxlen=None):
    thislen = minlen
    while maxlen is None or thislen <= maxlen:
        for prod in itertools.product(alphabet, repeat=thislen):
            yield ''.join(prod)
        thislen += 1

#   Opens a txt file, 'test.txt' (rename this for your usage) outputs/saves the programs...
#   ...'allcombinations' list automatically, with linebreaks inserted for clean out-put.

sys.stdout = open("allcombos.txt", "w")

#  Add your list inputs here
#  'abcdefghijklmnop0123456789!@#$%^&*-+_=~`' is listed by default
#  Specifiy your own *Min* and *Max* character lenghts for your project

for c in allcombos('!@#$%^&*-+_=~`abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-+_=~`', minlen=2, maxlen=2):
    print(c)
sys.stdout.close()

#END
