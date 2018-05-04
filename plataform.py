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
        
def cria_Plataform_Aleatoria():
    plataformas_group=pygame.sprite.Group()
    i=0
    while i<5:
        x=random.randint(0,500)
        y=random.randint(0,500)
        plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
        plataformas_group.add(plataforma1)
        i+=1
    return plataformas_group

def cria_Plataform_nAleatoria():
     plataformas_group=pygame.sprite.Group()
     plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [100, 500])        
     plataformas_group.add(plataforma1)
     plataforma2=Plataform("plataform_de_pedra_reta_pequena.png", [200, 500])        
     plataformas_group.add(plataforma2)
     plataforma3=Plataform("plataform_de_pedra_reta_pequena.png", [300, 500])        
     plataformas_group.add(plataforma3)
     plataforma4=Plataform("plataform_de_pedra_reta_pequena.png", [400, 500])        
     plataformas_group.add(plataforma4)
     plataforma5=Plataform("plataform_de_pedra_reta_pequena.png", [500, 500])        
     plataformas_group.add(plataforma5)
     return plataformas_group
     