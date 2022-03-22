#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    setColores = set(b)      
        
    if('_' in setColores ):        
        if(len(setColores) == 1):
            return "YES"
        else:
            setColores.remove('_')        
            for elem in setColores:
                if(b.count(elem) < 2):
                    return "NO"
            return "YES"
    else:
        if(len(setColores) == 1):
            if(len(b) > 1):
                return "YES"
            else:
                return "NO"
        else:
            for i in range(1,len(b)-1):
                if(not (b[i+1] == b[i] or b[i-1] == b[i])) :
                    return "NO"
            if(b[0] != b[1] or b[-1]!= b[-2]):
                return "NO"                    
            return "YES"        
        
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
