#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:46:15 2018

@author: manucastilla
"""
import pygame
import sys
from pygame.locals import *
pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Hello World')
fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
nome_jogo= movimento.bonequinho("starlego.png", 700, 500)
nome_jogo_group = pygame.sprite.Group()
nome_jogo_group.add(nome_jogo)
tela.blit(fundo, (0, 0))
pygame.display.update() 
