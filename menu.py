#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:46:15 2018

@author: manucastilla
"""
import pygame
import sys
from pygame.locals import *
import movimento
pygame.init()

tela2 = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Star Lego')
fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
iniciar_jogo = movimento.bonequinho("startgame.png", 125, 300)
iniciar_jogo_group=pygame.sprite.Group()

iniciar_jogo_group.add(iniciar_jogo)
nome_jogo= movimento.bonequinho("starlego.png", 125, 180)
nome_jogo_group=pygame.sprite.Group()
nome_jogo_group.add(nome_jogo)



tela2.blit(fundo, (0, 0))
nome_jogo_group.draw(tela2)
pygame.display.update() 
