# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:47:11 2018

@author: Amanda
"""

import pygame
import movimento
from pygame.locals import *

pygame.init()
pygame.font.init()

x=True
inicio_jogo=True
yellow = (255,255,0)

while x:
    if inicio_jogo==False:
                      tela3=pygame.display.set_mode((800,600),0,32)
                      pygame.display.set_caption('Star Lego')
                      fundo1 = pygame.image.load("Fundo-Estrelas.jpg").convert()
                      nome_do_jogador=movimento.bonequinho("nome_jogador.png", 110,200)
                      nome_do_jogador_group=pygame.sprite.Group()
                      nome_do_jogador_group.add(nome_do_jogador)
                      tela3.blit(fundo1, (0, 0))
                      nome_do_jogador_group.draw(tela3)
                      fonte=pygame.font.SysFont(None,25, None)
                      done=False
                      name=''
                      input_box=pygame.Rect(280,300,140,32)
                      
                      
                      for event in pygame.event.get():
                          if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_RETURN:
                                  done=True
                              if done:                 
                                  if event.key == pygame.K_RETURN:
                                     jogo=True
                                     jogador=False
                                  elif event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                                         x = False
                                  elif event.key == pygame.K_BACKSPACE:
                                     name = name[:-1]
                                  else:
                                      name += event.unicode
                                      print(name)  
                                      
                      txt_surface=fonte.render(name, True, yellow)
                      width= max(200,txt_surface.get_width()+10)
                      input_box.w=width
                      tela3.blit(txt_surface, (input_box.x+5, input_box.y+5))
                      pygame.draw.rect(tela3, yellow, input_box, 2)
                      
                      pygame.display.update()   
                                                           
pygame.display.quit()    