# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 19:43:50 2021

@author: Dr. Mota Liz
"""

import numpy as np

entradas = np.array ([4, 3])
pesos = np.array ([0.21, 0.22])
def soma (e, p):
    return e.dot(p)  
        
s = soma(entradas, pesos)    
def stepFuntion(soma):
    if (soma >= 1):
        return 1
    return 0
r = stepFuntion(s)