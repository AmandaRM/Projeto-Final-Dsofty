import pygame
import sys
from pygame.locals import *
from random import randrange
import plataform
import movimento

# ===============   INICIALIZAÇÃO   ===============
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Nome do joguinho')


#fazendo o chão do jogo
fundo = pygame.image.load("chão.png").convert()

# cria o bonzinho 
bonzinho = movimento.bonequinho("adventurer_stand.png", 1, 450)
bonzinho_group = pygame.sprite.Group()
bonzinho_group.add(bonzinho)
#cria o malvado
malvado= movimento.bonequinho("zombie_stand.png", 700, 1)
malvado_group=pygame.sprite.Group()
malvado_group.add(malvado)
#cria o portal=objetivo
portal=movimento.bonequinho("portal.png", 0, 0)
portal_group = pygame.sprite.Group()
portal_group.add(portal)

Plataforma=plataform.cria_Plataform_nAleatoria()
black=(0,0,0)

def gameover():
    fonte=pygame.font.SysFont(None, 25) #25 é o tamanho da mensagem
    text=fonte.render("Fim de jogo", True, black)
    tela.blit(text,(150,250))
# ===============   LOOPING PRINCIPAL   ===============

rodando = True
while rodando:
  for event in pygame.event.get():  #pega lista de eventos
      #gravidade = True
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
  
  gravidade=10 
  pygame.Rect.collidepoint
  
  pressed_keys=pygame.key.get_pressed()
  if pressed_keys[K_UP]:         
      bonzinho=movimento.bonequinho.bom_UP(bonzinho)
  elif pressed_keys[K_LEFT]:
      bonzinho=movimento.bonequinho.bom_LEFT(bonzinho)
  elif pressed_keys[K_RIGHT]:
      bonzinho=movimento.bonequinho.bom_RIGHT(bonzinho)
      
  elif pressed_keys[K_w]:
      malvado=movimento.bonequinho.pulando(malvado)
  elif pressed_keys[K_a]:
      malvado=movimento.bonequinho.bom_LEFT(malvado)
  elif pressed_keys[K_d]:
      malvado=movimento.bonequinho.bom_RIGHT(malvado)  
      
  elif bonzinho.rect.y>=0:
      gameover()

  #gera saídas
  tela.blit(fundo, (0, -85))
  bonzinho_group.draw(tela)
  malvado_group.draw(tela)
  portal_group.draw(tela)
  Plataforma.draw(tela)
  pygame.display.update()      #coloca a tela na janela
  
  bonzinho.rect.y+=bonzinho.vel
  bonzinho.vel+=0.001
  
  malvado.rect.y+=malvado.vel
  malvado.vel+=0.001
  
relogio=pygame.time.Clock()
tempo=relogio.tick(30)  
    
pygame.display.quit()