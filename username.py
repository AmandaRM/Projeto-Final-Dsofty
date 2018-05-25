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

def inserir_nome(screen, screen_size, events, maz_lenght=10,
                 font_style='None', font_size=35, font_color=yellow):
    fonte=pygame.font.SysFont(font_style, font_size)
    
    #pega o texto para colocar no centro da tela
    screen_lenght = screen_size[0]
    screen_height = screen_size[1]
    
    text_posX, text_posY, text_lenght, text_height = rendered_text.get_rect()
    
    #blitting o texto na tela
    screen.blit(rendered_text
                (screen_lenght/2 - text_lenght/2, screen_height/2 - text_height))

     #pegar o nome do usuário
    for event in events:
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RETURN:
                 return nome
             elif event.key == pygame.K_BACKSPACE:
                 nome = nome[:-1]
             elif event.unicode in ACCEPTED:
                 if len(name) < max_lenght:
                     nome += event.unicode
    player_name = font.render(name, True, RED)
    name_posX, name_posY, name_lenght, name_height = player_name.get_rect()
    screen.blit(player_name,
                (screen_lenght/2 - name_lenght/2, screen_height/2 + 100))
    
    return name
     
     
pygame.init()
tecla_pressionada = pygame.key.get_pressed()