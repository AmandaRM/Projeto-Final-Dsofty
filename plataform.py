# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:52:20 2018

@author: Amanda
"""
import pygame
import random

class Plataform (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, dimension):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = dimension[0]
        self.rect.y = dimension[1]
        
def cria_Plataform():
    plataformas_group=pygame.sprite.Group()
    i=0
    while i<5:
        x=random.randint(0,600)
        y=random.randint(0,800)
        plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
        plataformas_group.add(plataforma1)
        i+=1
        return plataformas_group