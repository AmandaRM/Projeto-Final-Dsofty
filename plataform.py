# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:52:20 2018

@author: Amanda
"""
import pygame

class Plataform (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, dimension):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = dimension[0]
        self.rect.y = dimension[1]
        
#def cria_Plataform:
 #   i=0
  #  while