# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:48:06 2018

@author: Amanda
"""
import pygame
########### MAPA #############

class Mapa (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, dimension):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(arquivo_imagem)
        self.rect.certerx=dimension[0]
        self.rect.certery=dimension[1]
        
