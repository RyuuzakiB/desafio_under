#Problema 2

#biblioteca que simplifica operações com matrizes
import numpy as np

#imprime matriz usada
matriz = [[1,2,3],[4,5,6],[7,8,-9]]
for i in matriz:
    for j in i:
        print(j, end='  ')
    print()
	
trace = np.asarray(matriz) #calcula soma da diagonal
trace_flip = np.fliplr(trace)  #calcula soma da diagonal inversa
diagonal_sum=abs(np.trace(trace))
antidiagonal_sum=abs(np.trace(trace_flip))
dif=diagonal_sum+antidiagonal_sum
print('Diferença absoluta entre as somas das duas diagonais: {}'.format(dif))