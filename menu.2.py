#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 11:15:39 2018

@author: manucastilla
"""

import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0, 0, 0)

tela2 = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Star Lego')
fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()

def game_intro():
    intro = True
    
    while intro:
        tela2.fill(white)
        message_to_screen("Bem vindo a Star Lego", black, -100)
        