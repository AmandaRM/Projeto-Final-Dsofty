import pygame
import sys
from pygame.locals import *
from random import randrange
import plataform
import movimento
import menu

# ===============   INICIALIZAÇÃO   ===============
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('LEGO Galaxy')


#fazendo o chão do jogo
fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
#fazer virar grupo

# cria o bonzinho 
bonzinho = movimento.bonequinho("adventurer_stand.png",700 ,520)
bonzinho_group = pygame.sprite.Group()
bonzinho_group.add(bonzinho)
#cria o malvado
malvado= movimento.bonequinho("zombie_stand.png", 700, 1)
malvado_group=pygame.sprite.Group()
malvado_group.add(malvado)
#cria o portal=objetivo
portal=movimento.bonequinho("portal.png", 4, 0)
portal_group = pygame.sprite.Group()
portal_group.add(portal)
portal_image=pygame.image.load("portal.png").convert()

chao=movimento.bonequinho("chão.png", 0, 570)
chao_group= pygame.sprite.Group()
chao_group.add(chao)

Plataforma=plataform.cria_Plataform_Aleatoria()

black=(0,0,0)
white = (255, 255, 255)

def gameover():
    fonte=pygame.font.SysFont(None,25) #25 é o tamanho da mensagem
    text=fonte.render("Fim de jogo", True, white)
    return tela.blit(text,(400,400))
    
cont=0
# ===============   LOOPING PRINCIPAL   ===============

rodando = True
relogio=pygame.time.Clock()
while rodando:
    
  tela.blit(fundo, (0, -85))
  chao_group.draw(tela)
  bonzinho_group.draw(tela)
  malvado_group.draw(tela)
  portal_group.draw(tela)
  Plataforma.draw(tela)
  pygame.display.update() 

  tempo=relogio.tick(30) 

  portal=movimento.bonequinho("portal.png", 0,0)
  #portal=pygame.transform.rotate(, 90)=================================
  portal_group= pygame.sprite.Group()
  portal_group.add(portal)

    
  for event in pygame.event.get():  #pega lista de eventos 0)

#  fonte=pygame.font.SysFont(None,25, None)
#    text=fonte.render(cont, "TIME: ", True, white)
#    tela.blit(text, (20,20)) 
   
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
    if event.type == pygame.KEYDOWN:
        if event.key == K_UP:
             bonzinho=movimento.bonequinho.bom_UP(bonzinho)
             bonzinho.image = pygame.image.load("adventurer_jump.png")
    if event.type == pygame.KEYUP:
        if event.key == K_RIGHT:
            bonzinho.image = pygame.image.load("adventurer_stand.png")
    if event.type == pygame.KEYUP:
        if event.key == K_LEFT:
            bonzinho.image = pygame.image.load("adventurer_stand.png")
    if event.type == pygame.KEYUP:
        if event.key == K_UP:
            bonzinho.image = pygame.image.load("adventurer_stand.png")
            

 #===========================COLLIDE=========================================#           
            



#  if pygame.sprite.spritecollide(Plataf, portal_group, True):
#      continue
#            


  if pygame.sprite.spritecollide(bonzinho, Plataforma, False):
      bonzinho.vel = 0
      
  if pygame.sprite.spritecollide(malvado, Plataforma, False):
      malvado.vel = 0 
      
  if pygame.sprite.spritecollide(bonzinho, chao_group, False):
      bonzinho.vel = 0
      
  if pygame.sprite.spritecollide(malvado, chao_group, False):
      malvado.vel = 0
      
  if pygame.sprite.spritecollide(malvado, bonzinho_group, True):
        malvado.vel = 0
        gameover()
        rodando  = False
        
  if pygame.sprite.spritecollide(portal,bonzinho_group, True):
      malvado.vel = 0
              
#  if pygame.sprite.spritecollide(portal, malvado_group, True) or  pygame.sprite.spritecollide(portal, bonzinho_group, True):
#      malvado.vel = 0

      #----------------------passar de fase---------------------
      
#  if pygame.sprite.spritecollide(malvado, bonzinho, True):
#      gameover()
      
  pressed_keys=pygame.key.get_pressed()     
  if pressed_keys[K_LEFT]:
      bonzinho=movimento.bonequinho.bom_LEFT(bonzinho)
      bonzinho.image = pygame.image.load("adventurer_walk2.png")
  elif pressed_keys[K_RIGHT]:
      bonzinho=movimento.bonequinho.bom_RIGHT(bonzinho)
      bonzinho.image = pygame.image.load("adventurer_walk1.png")

#  elif pressed_keys[K_a]:
#      malvado=movimento.bonequinho.bom_LEFT(malvado)
#  elif pressed_keys[K_d]:
#      malvado=movimento.bonequinho.bom_RIGHT(malvado)  

  if bonzinho.rect.x > malvado.rect.x:
     malvado=movimento.bonequinho.bom_RIGHT_light(malvado)
     malvado.image = pygame.image.load("zombie_walk1.png")
  if bonzinho.rect.x < malvado.rect.x:
     malvado=movimento.bonequinho.bom_LEFT_light(malvado)
     malvado.image = pygame.image.load("zombie_walk2.png") 
  if bonzinho.rect.y < malvado.rect.y:
      malvado=movimento.bonequinho.bom_UP_light(malvado)
      malvado.image = pygame.image.load("zombie_jump.png") 
      

      
      
  #gera saídas
     #coloca a tela na janela
  
  bonzinho.rect.y+=bonzinho.vel
  bonzinho.vel+=2
  
  malvado.rect.y+=malvado.vel
  malvado.vel+=2

cont+=1  
#menu.game_menu()
pygame.display.quit()