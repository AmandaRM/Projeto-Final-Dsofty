# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:44:50 2018

@author: gi_gi
"""

from firebase import firebase 
firebase=firebase.firebase.Application('https://projetofinal-d0c28.firebaseio.com/', None)

if firebase.get('Score', None) is None:
    score={}
else:
    score=firebase.get('Score', None)
    
<<<<<<< HEAD
if gameover == True:
    if nome in score:
        nome[minu]=minu
        nome[seg]=seg
    else:
        nome={}
        score=nome
        nome[minu]=minu
        nome[seg]=seg
           
    
=======
    
    
    

>>>>>>> a117ccdac650c211cc2cbabe4255cd797cabaac2
firebase.patch('https://projetofinal-d0c28.firebaseio.com/', score)
