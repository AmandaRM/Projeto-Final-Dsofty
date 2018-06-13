# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:22:46 2018

@author: Amanda
"""

def intercalar(lista1,lista2):
    if len(lista1)<=len(lista2):
        index=len(lista1)
    elif len(lista2)<len(lista1):
        index=len(lista2)
    lista3=[]
    i=0
    while i<index:
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        i+=1
    return lista3

lista1=[2,2,2,2]
lista2=[3,3,3,7,7,7]
#print(intercalar(lista1,lista2))

#numero=1
#while numero<101:
#    if numero%3==0:
#        if numero%5==0:
#            print("FizzBuzz")
#        else:
#            print("Fizz")
#    elif numero%5==0:
#        print("Buzz")
#    else:
#        print(numero)
#    numero+=1
#    
#def harshad(numero):
#    if numero ==0:
#        return False
#    numero=srt(numero)
#    index=len(numero)
#    i=0
#    soma=0
#    while i<index:
#        soma+=int(numero[i])
#        i+=1
##    elif int(numero)%soma==0:
#        return True
#    else:
#        return False
#    
#print(harshad(3))

def conta_string(lista):
    dicio={}
    for e in lista:
        if e in dicio:
            dicio[e]+=1
        else:
            dicio[e]=1           
    return dicio


lista1=['c', 'c', 'c', 'd', 'd', 'k', 'l', 'l']
print(conta_string(lista1))



