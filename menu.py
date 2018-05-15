#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:46:15 2018

@author: manucastilla
"""
import pygame
import time


def game_menu():
    introducao = True
    white = (255,255,255)
    while introducao:
        for evento in pygame.event.get():
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