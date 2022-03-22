#https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=false

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    maxBrr = max(b)
    factoresB = set()
    for i in range(1,maxBrr+1):
        if(ComprobarSiDivideATodos(i,b)):
            factoresB.add(i)
    
    return len(ComprobarFactoresA(factoresB,a))
                    
def ComprobarSiDivideATodos(num,arr):
    for elem in arr:
        if(elem % num != 0):
            return False
    return True            

def ComprobarFactoresA(setB,arr):
    factoresA = set()
    factBGreater = [x for x in setB if x >= max(arr)]
    for elem in factBGreater:
        if(EsFactorDeTodos(elem,arr)):
            factoresA.add(elem)
    print(factoresA)
    return factoresA        
            
def EsFactorDeTodos(num,arr):   
    print("array ", arr, "numero ", num)
    for elem in arr:
        if(num%elem != 0):
            return False
    return True

if __name__ == '__main__':
    n = 1
    m = 1
    arr = [1]
    brr = [100]
    total = getTotalX(arr, brr)
    print("total ",total)

