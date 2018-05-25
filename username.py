#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:13:51 2018

@author: manucastilla
"""

import pygame
import string
from pygame.locals import *

yellow = (255,255,0)

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "

def inserir_nome():
    nome=[]
     #pegar o nome do usuário
    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RETURN:
                 return nome
             elif event.key == pygame.K_BACKSPACE:
                 nome = nome[:-1]
             elif event.unicode in ACCEPTED:
                 if len(nome) < 11:
                     nome += event.unicode
    return nome
     
    
pygame.init()
tecla_pressionada = pygame.key.get_pressed()