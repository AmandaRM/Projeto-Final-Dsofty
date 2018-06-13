# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:22:41 2018

@author: Amanda
"""

dic={"batata":1, "alface":2, "atum":4, "cebola":3}
lista=['atum', 'alface']

def preco(dicionario, lista):
    soma=0
    for e in lista:
        if e in dicionario:
            soma+=dicionario[e]
    return soma

print(preco(dic,lista))        