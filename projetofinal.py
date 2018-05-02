import pygame
import sys
from pygame.locals import *
from random import randrange

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
    
# ===============   INICIALIZAÇÃO   ===============
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Pygame')

# carrega imagem de fundo
fundo = pygame.image.load("fundo_verde.png").convert()

# cria o bonzinho 
bonzinho = bonzinho("adventurer_stand.png", 0, 450)
bonzinho_group = pygame.sprite.Group()
bonzinho_group.add(bonzinho)
#cria o malvado
malvado= malvado("zombie_stand.png", 700, 0)
malvado_group=pygame.sprite.Group()
malvado_group.add(malvado)


# ===============   LOOPING PRINCIPAL   ===============

rodando = True
while rodando:
  
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
      
  #move o bonzinho pela tela
  pressed_keys=pygame.key.get_pressed()   
  if pressed_keys[K_UP]:
      bonzinho.rect.y-=1
  elif pressed_keys[K_DOWN]:
      bonzinho.rect.y+=1
  elif pressed_keys[K_LEFT]:
      bonzinho.rect.x-=1
  elif pressed_keys[K_RIGHT]:
      bonzinho.rect.x+=1
      
  #move o malvado
  pressed_keys=pygame.key.get_pressed()   
  if pressed_keys[K_w]:
      malvado.rect.y-=1
  elif pressed_keys[K_s]:
      malvado.rect.y+=1
  elif pressed_keys[K_a]:
      malvado.rect.x-=1
  elif pressed_keys[K_d]:
      malvado.rect.x+=1
  
 

        
  #gera saídas
  tela.blit(fundo, (0, 0))
  bonzinho_group.draw(tela)
  malvado_group.draw(tela)
  pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()