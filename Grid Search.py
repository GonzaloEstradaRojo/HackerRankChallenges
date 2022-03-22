#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    numFilasG = len(G) #Num filas G
    numFilasP = len(P) #Num filas P
    numColsG = len(G[0]) #Num cols G
    numColsP = len(P[0]) #Num cols P

    # for i in range(numFilasG):
    #     iteraciones = 0
    #     indexini = G[i].find(P[0])
    #     if(indexini == -1):
    #         continue        
    #     for j in range(numFilasP):
    #         if(G[i+j][indexini:indexini+numColsP] != P[j]):
    #             break        
    #         iteraciones += 1
    #     if (iteraciones == numFilasP):
    #         return "YES"    
    # return "NO"
                
    for i in range(numFilasG):
        indices = [ind for ind in range(len(G[i]) - len(P[0]) + 1 ) if G[i][ind:ind+len(P[0])] == P[0]]
        print(indices)
        for indice in indices:
            iteraciones = 0
            for j in range(numFilasP):
                if(G[i+j][indice:indice+numColsP] != P[j]):
                     break                    
                iteraciones += 1
            if (iteraciones == numFilasP):
                return "YES" 
                        
    return "NO"
    

if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

