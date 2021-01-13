# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:47:06 2021

@author: wkevi
"""

str1='Cisco'
str2='Networking'
str3='Academy'
space=""
x=5
print(str1+str2+str3+space)
print('\n')
print(str1+str2+str3,'\n'*2)
print(str1,str2,str3,'\n'*2)
print('El valor de x es: ',x)
print('El valor de x es: '+str(x))
print(type(x))
x=str(x)
print(type(x))
x=int(x)
print(type(x))
x=float(x)
print(type(x))
x=bool(x)
print(type(x))