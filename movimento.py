# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:03:19 2018

@author: Amanda
"""
import pygame

# ===============      CLASSES      ===============
class bonzinho(pygame.sprite.Sprite):
  
  def __init__(self, arquivo_imagem, pos_x, pos_y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(arquivo_imagem)
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y
    
 
# ===============      CLASSES      ===============
class malvado(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

####### fazer funções em que cada função é um movimento #####
def bom_UP():
      bonzinho.rect.y-=1

def bom_LEFT():
        bonzinho.rect.x-=1

def bom_RIGHT():
        bonzinho.rect.x+=1
