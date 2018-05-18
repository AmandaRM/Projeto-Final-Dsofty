#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:46:15 2018

@author: manucastilla
"""
import pygame
pygame.init()
import pygameMenu
from pygameMenu.locals import*

def menu(self):
    count = 0
    pygame.mouse.set_visible(1)
    p1 = Botao(400,300,"1p.png")
    p2 = Botao(400,300,"2p.png")
    ex = Botao(400,500,"sair.png")
    cursor = Cursos([0,0])
    botoes = []
    botoes.append(p1)
    botoes.append(p2)
    botoes.append(ex)
    while 1:
        count+=1
        self.clock.tick(600)
    


"""
pygameMenu.Menu(surface, window_width, windw_height, font, title, *args) # -> Menu object

def game_menu():
    introducao = True
    white = (255,255,255)
    while introducao:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("jogo da porra", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(15)
    
game_menu()
"""