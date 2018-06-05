#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:13:51 2018

@author: manucastilla
"""

import pygame
import string
from pygame.locals import *

#yellow = (255,255,0)
#
#ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "
#
#def inserir_nome():
#    nome="usuario"
#    nome_inserido=" "
#     #pegar o nome do usuário
#    for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 return nome
#             elif event.key == pygame.K_BACKSPACE:
#                 nome_inserido = nome_inserido[:-1]
#             elif event.unicode in ACCEPTED:
#                 if len(nome_inserido) < 12:
#                     return event.unicode


RED = (182, 38, 37)
BLACK = (0, 0, 0)
WHITE = (252, 252, 252)
pygame.font.init()

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "

def textInputBox(name, screen, screen_size, events, turn, font, max_lenght=10):
    
    # Preparing the Screen
    screen.fill(BLACK)    
    
    # Rendering the basic texts
    if turn == 1:
        text1 = "Please Type Player 1's Name."
    rendered_text1 = font.render(text1, True, RED)

    
    # Gets the text rect, so we can center it to the screen
    screen_lenght = screen_size[0]
    screen_height = screen_size[1]
    
    text_posX1, text_posY1, text_lenght1, text_height1 = rendered_text1.get_rect()

    
    # Blitting the basic texts on screen
    screen.blit(rendered_text1,
                (screen_lenght/2 - text_lenght1/2, screen_height/2 - text_height1))

    # Getting players name
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return name
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.unicode in ACCEPTED:
                if len(name) < max_lenght:
                    name += event.unicode
    
    # Rendering Player's name and getting its positions
    player_name = font.render(name, True, RED)
    name_posX, name_posY, name_lenght, name_height = player_name.get_rect()
    
    # Blitting the player Name
    screen.blit(player_name)
    
    return name


#          nome=""
#          if len(nome) < 12:
#              retorno= username.inserir_nome()
#              print(retorno)
#              nome.append(retorno)
#              fonte_style=pygame.font.SysFont(None,35)
#              textnome = fonte_style.render(str(nome), True, yellow)
#              tela2.blit(textnome, (350,450))
#          if len(nome) == 1:
#              fonte_style=pygame.font.SysFont(None,35)
#              textnome = fonte_style.render("insira seu nome", True, yellow)
#              tela2.blit(textnome, (350,450))