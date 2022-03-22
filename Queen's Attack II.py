# #https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'queensAttack' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. INTEGER k
# #  3. INTEGER r_q
# #  4. INTEGER c_q
# #  5. 2D_INTEGER_ARRAY obstacles
# #

# def queensAttack(n, k, r_q, c_q, obstacles):
#     # Write your code here
#     print(getFila(n,r_q, c_q, obstacles))
#     casillasHorizontales = getFila(n,r_q, c_q, obstacles)
#     print(getColumna(n,r_q, c_q, obstacles))
#     casillasVerticales = getColumna(n,r_q, c_q, obstacles)
#     print("Sup Der " ,getDiagonalSupDer(n,r_q, c_q, obstacles))
#     casillasDiagSupDer = getDiagonalSupDer(n,r_q, c_q, obstacles)
#     print("Sup Izq " ,getDiagonalSupIzq(n,r_q, c_q, obstacles))
#     casillasDiagSupIzq = getDiagonalSupIzq(n,r_q, c_q, obstacles)
#     print("Inf Der " ,getDiagonalInfDer(n,r_q, c_q, obstacles))
#     casillasDiagInfDer = getDiagonalInfDer(n,r_q, c_q, obstacles)
#     print("Inf Izq " ,getDiagonalInfIzq(n,r_q, c_q, obstacles))
#     casillasDiagInfIzq = getDiagonalInfIzq(n,r_q, c_q, obstacles)
#     return(len(casillasHorizontales) + len(casillasVerticales) + len(casillasDiagSupDer) + len(casillasDiagSupIzq) + len(casillasDiagInfDer) + len(casillasDiagInfIzq) )
    
# def getFila(n,r_q,c_q,obstacles):
#     casillasHorizontales = []
#     for i in range(c_q-1,0,-1):
#         if [r_q,i] in obstacles:
#             break
#         casillasHorizontales.append([r_q,i])
        
#     for i in range(c_q+1, n+1):
#         if [r_q,i] in obstacles:
#             break
#         casillasHorizontales.append([r_q,i])
        
#     return casillasHorizontales
        
# def getColumna(n,r_q,c_q,obstacles):
#     casillasVerticales = []
#     for i in range(r_q-1,0,-1):
#         if [i,c_q] in obstacles:
#             break
#         casillasVerticales.append([i,c_q])
        
#     for i in range(r_q+1, n+1):
#         if [i,c_q] in obstacles:
#             break
#         casillasVerticales.append([i,c_q])
        
#     return casillasVerticales

# def getDiagonalSupDer(n,r_q,c_q,obstacles):
#     casillasDiagSupDer = []
#     minDisFilaCol = min(n-r_q,n-c_q)
#     for i in range(minDisFilaCol):
#         if [r_q+(1+i),c_q+(1+i)] in obstacles:
#             break
#         casillasDiagSupDer.append([r_q+1+i,c_q+1+i])
#     return casillasDiagSupDer
        

# def getDiagonalSupIzq(n,r_q,c_q,obstacles):
#     casillasDiagSupIzq = []
#     minDisFilaCol = min(n-r_q,c_q-1)
#     for i in range(minDisFilaCol):
#         if [r_q+(1+i),c_q-(1+i)] in obstacles:
#             break
#         casillasDiagSupIzq.append([r_q+(1+i),c_q-(1+i)])
#     return casillasDiagSupIzq
        
# def getDiagonalInfDer(n,r_q,c_q,obstacles):
#     casillasDiagInfDer = []
#     minDisFilaCol = min(r_q-1,n-c_q)
#     for i in range(minDisFilaCol):
#         if [r_q-(1+i),c_q+(1+i)] in obstacles:
#             break
#         casillasDiagInfDer.append([r_q-(1+i),c_q+(1+i)])
#     return casillasDiagInfDer

# def getDiagonalInfIzq(n,r_q,c_q,obstacles):
#     casillasDiagInfIzq = []
#     minDisFilaCol = min(r_q-1,c_q-1)
#     for i in range(minDisFilaCol):
#         if [r_q-(1+i),c_q-(1+i)] in obstacles:
#             break
#         casillasDiagInfIzq.append([r_q-(1+i),c_q-(1+i)])
#     return casillasDiagInfIzq
               
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     second_multiple_input = input().rstrip().split()

#     r_q = int(second_multiple_input[0])

#     c_q = int(second_multiple_input[1])

#     obstacles = []

#     for _ in range(k):
#         obstacles.append(list(map(int, input().rstrip().split())))

#     result = queensAttack(n, k, r_q, c_q, obstacles)

#     fptr.write(str(result) + '\n')

#     fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    return CheckObstaculosInDirection(n,r_q,c_q,obstacles)

    
def CheckObstaculosInDirection(n, r_q, c_q, obstacles):    
    
    obstaculoHorIzq = [r_q,0]
    obstaculoHorDer = [r_q,n+1]
    obstaculoVerSup = [n+1,c_q]
    obstaculoVerInf = [0,c_q]
    
    obstaculoDiagSupIzq = [r_q+(1+min(n-r_q,c_q-1)),c_q-(1+min(n-r_q,c_q-1))]
    obstaculoDiagSupDer = [r_q+(1+min(n-r_q,n-c_q)),c_q+(1+min(n-r_q,n-c_q))]
    obstaculoDiagInfIzq = [r_q-(1+min(r_q-1,c_q-1)),c_q-(1+min(r_q-1,c_q-1))]
    obstaculoDiagInfDer = [r_q-(1+min(r_q-1,n-c_q)),c_q+(1+min(r_q-1,n-c_q))]
    
    difReina = r_q - c_q  
    sumaReina = r_q + c_q  
                
    print(obstaculoHorIzq, obstaculoHorDer,obstaculoVerSup,obstaculoVerInf,obstaculoDiagSupIzq,obstaculoDiagSupDer,obstaculoDiagInfIzq,obstaculoDiagInfDer)
    
    for elemObs in obstacles: 
        if(elemObs[0] == r_q ):
            if(elemObs[1]< c_q and elemObs[1]>obstaculoHorIzq[1]):
                obstaculoHorIzq = elemObs
            elif(elemObs[1]> c_q and elemObs[1]<obstaculoHorDer[1]): 
                obstaculoHorDer = elemObs
        elif(elemObs[1] == c_q ):
            if(elemObs[0] < r_q and elemObs[0]>obstaculoVerInf[0]):
                obstaculoVerInf = elemObs
            elif(elemObs[0] > r_q and elemObs[0]<obstaculoVerSup[0]): 
                obstaculoVerSup = elemObs
        elif(elemObs[0]-elemObs[1] == difReina):
            if(elemObs[0] < obstaculoDiagSupDer[0] and elemObs[0] > r_q ):
                obstaculoDiagSupDer = elemObs
            elif(elemObs[0] > obstaculoDiagInfIzq[0] and elemObs[0] < r_q):
                obstaculoDiagInfIzq = elemObs
        elif(elemObs[0]+elemObs[1] == sumaReina):
            if(elemObs[0] < obstaculoDiagSupIzq[0] and elemObs[0] > r_q ):
                obstaculoDiagSupIzq = elemObs
            elif(elemObs[0] > obstaculoDiagInfDer[0] and elemObs[0] < r_q):
                obstaculoDiagInfDer = elemObs
    
                
    
    pasosHorIzq = c_q - obstaculoHorIzq[1] - 1
    pasosHorDer = obstaculoHorDer[1] - c_q - 1
    pasosVerSup = obstaculoVerSup[0] - r_q - 1
    pasosVerInf = r_q - obstaculoVerInf[0] - 1 
    pasosDiagSupDer = obstaculoDiagSupDer[0] - r_q - 1
    pasosDiagSupIzq = obstaculoDiagSupIzq[0] - r_q - 1
    pasosDiagInfDer = r_q - obstaculoDiagInfDer[0] - 1
    pasosDiagInfIzq = r_q - obstaculoDiagInfIzq[0] - 1
    
    print(obstaculoHorIzq, obstaculoHorDer,obstaculoVerSup,obstaculoVerInf,obstaculoDiagSupIzq,obstaculoDiagSupDer,obstaculoDiagInfIzq,obstaculoDiagInfDer)      
    print( pasosHorIzq,pasosHorDer,pasosVerSup,pasosVerInf,pasosDiagSupIzq,pasosDiagSupDer,pasosDiagInfIzq,pasosDiagInfDer)
    return pasosHorIzq+pasosHorDer+pasosVerSup+pasosVerInf+pasosDiagSupDer+pasosDiagSupIzq+pasosDiagInfDer+pasosDiagInfIzq
                
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    # fptr.write(str(result) + '\n')

    # fptr.close()
