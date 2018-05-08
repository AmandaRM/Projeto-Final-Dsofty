# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:03:19 2018

@author: Amanda
"""
import pygame
import time

# ===============      CLASSES      ===============
    

class bonequinho(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def pulando(self):
        for i in range(10):
            self.rect.y-=1
            return self
        for i in range(10):
            self.rect.y+=1
            time.sleep(0.01)
            return self

    def bom_UP(self):
        self.pulando = True
        self.pulando = False

    def bom_LEFT(self):
        if 0< self.rect.x <=750:
            self.rect.move_ip(-1,0) #move_ip(x,y)
            return self
        else:
            self.rect.move_ip(1,0)
            return self

    def bom_RIGHT(self):
        if 0<= self.rect.x <750:
            self.rect.move_ip(1,0) #move_ip(x,y)
            return self
        else:
            self.rect.move_ip(-1,0)
            return self
    
