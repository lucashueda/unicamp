# Biblioteca de funções para  o projeto de MS512 - Análise numérica 2s2019

# aqui terão todas as funções necessárias para o projeto

import numpy as np
import pandas as pd

# Definindo uma classe Cholesky, que realizará todas as etapas de cholesky, desde a fatoração até a resolução de um sistema
class Cholesky():
    
    A = 0
    
    def __init__(self,M):
        self.A = M
    
    def get_A(self):
        return self.A
    
    def set_A(self,M):
        self.A = M
    
    def cholesky_factor(self,):
        
        
    
    n = A.shape[0], m = A.shape[1]
    
    
# Definindo uma classe Householder, que realizará todas as etapas da fatoração QR via refletores
class HouseHolder():
    
    A = 0
    
    def __init__(self,M):
        self.A = M
        
        
# Definindo uma classe GramSchmdit, que realizará todas as etapas da fatoração QR via GramSchmdit
class GramSchmdit():
    
    A = 0
    
    def __init__(self,M):
        self.A = M