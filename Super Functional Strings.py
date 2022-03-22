#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superFunctionalStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def superFunctionalStrings(s):
    # Write your code here
    
    longitud = len(s)
    result = 0
    distintSubstring = set()
    for i in range(longitud):
        for j in range(longitud-i):
            distintSubstring.add(s[j:j+i+1])
            
    for elem in distintSubstring:
        dis = len(set(elem))
        result += (len(elem)**dis)%(1e9+7)
            

    return int(result%(1e9+7))
            
if __name__ == '__main__':

    result = superFunctionalStrings("aaabbbdddfffggghhhiiikkkmmmnnnooopppqqqrrrssstttuuuvvvwwwyyyzzzpynkfabmhodz")
    print(result)
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = superFunctionalStrings(s)
        print(result)

