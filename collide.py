# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:31:22 2018

@author: gi_gi
"""
import pygame


def collide(self, xvel, yvel, plataform):
    if pygame.sprite.collide_rect(self, plataform.rect):
        if xvel > 0:
            self.rect.right = plataform.rect.left
        if xvel< 0 :
            self.rect.left = plataform.rect.right
        if yvel > 0:
            self.rect.bottom=plataform.rect.top
            self.onGround=True 
            self.yvel=0
        if yvel<0:
            self.rect.top = plataform.rect.bottom
            