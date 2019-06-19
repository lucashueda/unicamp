# Biblioteca de funções para  o projeto de MS512 - Análise numérica 2s2019

# Aqui terão todas as funções necessárias para o projeto

import utils as ut
import numpy as np
import pandas as pd

# Definindo uma classe HouseHolder, que realizará todas as etapas da decomposição QR por refletores, desde a fatoração até a resolução de um sistema
class HouseHolder():
    
    
    def __init__(self,M):
        self.M = M
        
     
    def padding(self,A):
        
        '''
        
        Função que cria uma hora de zeros a esquerda e em cima na matriz A, e 1 onde for na região concatenada e i=j
        
        '''
        
        size = A.shape[0]
        
        result = np.zeros([size+1,size+1])
        
        result[1:A.shape[0]+1, 1:A.shape[1]+1] = A
        
        new_size = result.shape[0]

        for i in range(new_size-size):
            for j in range(new_size-size):
                if(i==j):
                    result[i,j] = 1
        
        return result
    
    def getQ(self,x):
        
        '''
        Função que retorna a matriz ortogonal Q para um dado vetor x de R^n onde,
        
        Qx = [-t,0,...,00]t
        
        
        '''
        
        # Checagem se x não é um vetor nulo
        
        u = x.copy()
        
        #print(u)
        #print(x)
        
        beta = max(u)
        
        if(beta == 0):
            return np.eye(len(u))
        else:
            tau = ut.norma2(x)
            #print(tau)
            #print(u[0])
            if(u[0] < 0):
                tau = -tau
            
            u[0] = tau +u[0]
            
            #print(u[0])
            gamma = u[0]/tau
            
            u =[i/u[0] for i in u]
              
            #print(np.linalg.norm(x))
            #print(tau)
            Q = np.eye(len(u)) - (2/np.dot(u,u))*np.dot(ut.transposta([u]), [u])
            
            return Q

        
    def getQR(self,A):
        
        R = np.array(A)
        
        n = len(A)
        
        Qf = np.eye(n)
        
        for i in range(n - 1):
            
            Qa = np.eye(n)
            Qa[i:, i:] = self.getQ(R[i:, i])
            Qf = np.dot(Qf,Qa)
            R = np.dot(Qa, R)
            
        return Qf, R
    
    def resolve_sistema_1d(self,b):
        b = np.array(b)
          
        return ut.retroSub(self.R, b)
    
    def resolve_sistema(self,b):
        b = np.array(b)
        
        Q, R = self.getQR(self.M)
        
        self.R = R
        
        b = np.dot(ut.transposta(Q),b)
        
        n = b.shape[0]
        
        if(len(b.shape) == 1):
            m = 1
        else:
            m = b.shape[1]
        
        resultado = np.eye(n)
        
        for i in range(m):
            resultado[:,i] = self.resolve_sistema_1d(b[:,i])
            
        return resultado
        
        