# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:38:03 2021

@author: wkevi
"""

lista=['R1',5,5.8,True,"R1"]
print(lista)
print(type(lista))
print(len(lista))
print(lista[0],'\n')
print(lista[4],'\n')
lista[3]=False
print(lista)
del lista[4]
print(lista)
lista.append("R2")
print(lista)
lista.append("R3")
print(lista)