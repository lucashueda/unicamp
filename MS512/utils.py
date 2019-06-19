# Pacote com funções auxiliares, transposta, normal, produto interno e resolução de sistema linear
#
#@Author: Lucas hideki Ueda, Inaye Caroline, Gustavo guedes

import pandas as pd
import numpy as np

def norma2(x):
    return np.sqrt(np.sum([x[i]**2 for i in range(len(x))]))
    
def produto_interno(x,y):
    
    if(len(x)!=len(y)):
        print("error: Os vetores tem tamanho diferentes.")
    else:
        return [x[i]*y[i] for i in range(len(x))]
    
def transposta(A):
    linhas = len(A)
    colunas = len(A[0])
    
    #if(linhas != colunas):
       # print("error: A matriz não é quadrada")
    
    return np.array([[ A[i][j] for i in range(linhas)] for j in range(colunas)])
    
def retroSub(A,b):
    
    n = len(A) 
    m = len(A[0]) 
    
    
    x = np.zeros(n)
    # Checando consistência A 
    
    # Resolvendo retro substituição para A triangular superior
    # Iniciando o último elemento
    x[n-1] = b[n-1]/A[n-1][n-1]
    
    soma = 0
    
    for i in range(n-2,-1,-1):
        soma = b[i]

        for j in range(i+1, n):
            soma = soma - A[i][j]*x[j]
            
        x[i] = soma/A[i][i]

    return x

def norma_mat1(A):
    
    A = np.array(A)
    
    

    
    if((A.shape == (int(A.shape[0]),)) | (A.shape[0] == 1)):

        return sum([np.abs(v) for v in A])
    
    c = []
    
    
    for i in range(A.shape[0]):
        c.append(sum([np.abs(v) for v in A[:,i]]))
    
    
    return np.max(c)

def getHilbert(n):
    
    A = np.zeros([n,n])
    
    for i in range(n):
        for j in range(n):
            A[i][j] = 1/(i+j+1)
            
    return A