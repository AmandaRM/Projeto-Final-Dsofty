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



"""    i=0
    plataformas_group=pygame.sprite.Group()
    while i<15:
        x=50
        y=100
        if i<=4:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)
        #x=100
        #y=200
        elif i<=7:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)
        #x=50
        #y=300
        elif i<=12:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)
        #x=100
        #y=400
        elif i<=15:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)        
        i+=1
    return plataformas_group
    """
def cria_Plataform_nAleatoria():
     plataformas_group=pygame.sprite.Group()
     plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [50, 400])        
     plataformas_group.add(plataforma1)
     plataforma2=Plataform("plataform_de_pedra_reta_pequena.png", [150, 100])        
     plataformas_group.add(plataforma2)
     plataforma3=Plataform("plataform_de_pedra_reta_pequena.png", [250, 400])        
     plataformas_group.add(plataforma3)
     plataforma4=Plataform("plataform_de_pedra_reta_pequena.png", [350, 100])        
     plataformas_group.add(plataforma4)
     plataforma5=Plataform("plataform_de_pedra_reta_pequena.png", [450, 400])        
     plataformas_group.add(plataforma5)
     plataforma6=Plataform("plataform_de_pedra_reta_pequena.png", [650, 400])        
     plataformas_group.add(plataforma6)
     plataforma7=Plataform("plataform_de_pedra_reta_pequena.png", [550, 100])        
     plataformas_group.add(plataforma7)
     
     plataforma8=Plataform("plataform_de_pedra_reta_pequena.png", [50, 200])        
     plataformas_group.add(plataforma8)
     plataforma9=Plataform("plataform_de_pedra_reta_pequena.png", [150, 300])        
     plataformas_group.add(plataforma9)
     plataforma10=Plataform("plataform_de_pedra_reta_pequena.png", [250, 200])        
     plataformas_group.add(plataforma10)
     plataforma11=Plataform("plataform_de_pedra_reta_pequena.png", [350, 300])        
     plataformas_group.add(plataforma11)
     plataforma12=Plataform("plataform_de_pedra_reta_pequena.png", [450, 200])        
     plataformas_group.add(plataforma12)
     plataforma13=Plataform("plataform_de_pedra_reta_pequena.png", [650, 200])        
     plataformas_group.add(plataforma13)
     plataforma14=Plataform("plataform_de_pedra_reta_pequena.png", [550, 300])        
     plataformas_group.add(plataforma14)
     
     plataforma15=Plataform("plataform_de_pedra_reta_pequena.png", [150, 500])        
     plataformas_group.add(plataforma15)
     plataforma16=Plataform("plataform_de_pedra_reta_pequena.png", [350, 500])        
     plataformas_group.add(plataforma16)
     plataforma17=Plataform("plataform_de_pedra_reta_pequena.png", [550, 500])        
     plataformas_group.add(plataforma17)
     return plataformas_group
