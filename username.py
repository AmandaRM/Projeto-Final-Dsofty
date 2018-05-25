#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:13:51 2018

@author: manucastilla
"""

import pygame
from pygame.locals import *
import sys
import sprites

def nome_usuario():
    pygame.init()

pygame.init()
fonte=pygame.font.SysFont(None,25)   
yellow = (255,255,0)
tecla_pressionada = pygame.key.get_pressed()
if tecla_pressionada[K_a]:
    text=fonte.render( "A", True, yellow)
    text.blit(tela2(125,450))
elif tecla_pressionada[K_b]:
    text=fonte.render( "B", True, yellow)
    text.blit(tela2(125,452))
elif tecla_pressionada[K_c]:
    text=fonte.render( "C", True, yellow)
elif tecla_pressionada[K_d]:
    text=fonte.render( "D", True, yellow)
elif tecla_pressionada[K_e]:
    text=fonte.render( "E", True, yellow)
elif tecla_pressionada[K_f]:
    text=fonte.render( "F", True, yellow)
elif tecla_pressionada[K_g]:
    text=fonte.render( "G", True, yellow)
elif tecla_pressionada[K_h]:
    text=fonte.render( "H", True, yellow)
elif tecla_pressionada[K_i]:
    text=fonte.render( "I", True, yellow)
elif tecla_pressionada[K_j]:
    text=fonte.render( "J", True, yellow)
elif tecla_pressionada[K_k]:
    text=fonte.render( "K", True, yellow)
elif tecla_pressionada[K_l]:
    text=fonte.render( "L", True, yellow)
elif tecla_pressionada[K_m]:
    text=fonte.render( "M", True, yellow)
elif tecla_pressionada[K_n]:
    text=fonte.render( "N", True, yellow)
elif tecla_pressionada[K_o]:
    text=fonte.render( "O", True, yellow)
elif tecla_pressionada[K_p]:
    text=fonte.render( "P", True, yellow)
elif tecla_pressionada[K_q]:
    text=fonte.render( "Q", True, yellow)
elif tecla_pressionada[K_r]:
    text=fonte.render( "R", True, yellow)
elif tecla_pressionada[K_s]:
    text=fonte.render( "S", True, yellow)
elif tecla_pressionada[K_t]:
    text=fonte.render( "T", True, yellow)
elif tecla_pressionada[K_u]:
    text=fonte.render( "U", True, yellow)
elif tecla_pressionada[K_v]:
    text=fonte.render( "V", True, yellow)
elif tecla_pressionada[K_w]:
    text=fonte.render( "W", True, yellow)
elif tecla_pressionada[K_x]:
    text=fonte.render( "X", True, yellow)
elif tecla_pressionada[K_y]:
    text=fonte.render( "Y", True, yellow)
elif tecla_pressionada[K_z]:
    text=fonte.render( "Z", True, yellow)