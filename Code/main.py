# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:51:57 2023

@author: Maisa
"""

frase = 'Abra a porta!' 
new_frase=[] 
for caracter in frase: 
  if (ord(caracter) >= 97 and ord(caracter) <= 119) or (ord(caracter) >= 65 and ord(caracter) <= 87): 
    new_car=ord(caracter)+3 
    new_frase.append(chr(new_car)) 
  elif (ord(caracter) >= 120 and ord(caracter) <= 122) or (ord(caracter)>= 88 and ord(caracter) <= 90): 
    new_car= ord(caracter)-23 
    new_frase.append(chr(new_car)) 
  else: 
    new_frase.append(caracter) 
print(''.join(new_frase))