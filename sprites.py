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
malvado= movimento.bonequinho("zombie_stand.png", 200, 1)
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

Plataforma, Plataformas_Amarelas, Plataformas_Vermelhas, Plataformas_Verdes =plataform.cria_Plataform_nAleatoria()

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
    
  tempo=relogio.tick(30)
  tempo_tela = 1000/tempo
    
  tela.blit(fundo, (0, -85))
  chao_group.draw(tela)
  bonzinho_group.draw(tela)
  malvado_group.draw(tela)
  portal_group.draw(tela)
  Plataforma.draw(tela)
  Plataformas_Amarelas.draw(tela)
  Plataformas_Vermelhas.draw(tela)
  Plataformas_Verdes.draw(tela)
  
  fonte=pygame.font.SysFont(None,25, None)
  text=fonte.render( "TIME: ", True, white)
  text2=fonte.render(cont , True, white)
  tela.blit(text, (700,20)) 
#  tela.blit(text, (720,20)) 
  
  pygame.display.update() 

  portal=movimento.bonequinho("portal.png", 0,0)
  #portal=pygame.transform.rotate(, 90)=================================
  portal_group= pygame.sprite.Group()
  portal_group.add(portal)

    
  for event in pygame.event.get():  #pega lista de eventos 0)


   
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
            
    def collide(self, x, y, plataform):
       if pygame.sprite.collide_rect(self, plataform.rect):
           if  xvel > 0:
               self.rect.right = plataform.rect.left
           if xvel< 0 :
               self.rect.left = plataform.rect.right
           if yvel > 0:
               self.rect.bottom=plataform.rect.top
               self.onGround=True 
               self.yvel=0
           if yvel<0:
               self.rect.top = plataform.rect.bottom
    collide()           
               
#       for e in Plataforma:
#        if pygame.sprite.collide_rect(bonzinho, e.rect):
#           if  bonzinho.rect.x  > 0:
#               bonzinho.rect.right = e.rect.left
#               bonzinho.vel=0
#           if bonzinho.rect.x < 0 :
#               bonzinho.rect.left = e.rect.right
#               bonzinho.vel=0
#           if bonzinho.rect.y > 0:
#               bonzinho.rect.bottom= e.rect.top
#               bonzinho.onGround=True 
#               bonzinho.vel=0
#           if bonzinho.rect.y < 0:
#               bonzinho.rect.top = e.rect.bottom
#               bonzinho.vel=0
               
               
       
    
#  if pygame.sprite.spritecollide(Plataf, portal_group, True):
#      continue
#            




#  if pygame.sprite.spritecollide(Plataf, portal_group, True):
#      continue
#            

  for e in Plataformas_Vermelhas:
      e=plataform.move_plataforma(e, 400, 200)

  listaColididos = pygame.sprite.spritecollide(bonzinho, Plataforma, False)
  if listaColididos:
      if listaColididos[0].rect.y > bonzinho.rect.y+bonzinho.rect.height:
          bonzinho.vel = 0
     
  if pygame.sprite.spritecollide(bonzinho, Plataformas_Verdes, True): #collide só para o pé do bicho
      bonzinho.vel = 3
      
  if pygame.sprite.spritecollide(bonzinho, Plataformas_Amarelas, False):
      bonzinho.vel = -3
    
  if pygame.sprite.spritecollide(bonzinho,Plataformas_Vermelhas, True):
      bonzinho.vel=2
      
  if pygame.sprite.spritecollide(malvado, Plataforma, False):
      malvado.vel = 0 
      
  if pygame.sprite.spritecollide(bonzinho, chao_group, False):
      bonzinho.vel = 0
      
  if pygame.sprite.spritecollide(malvado, chao_group, False):
      malvado.vel = 0
      
  if pygame.sprite.spritecollide(malvado, bonzinho_group, True):
        fonte=pygame.font.SysFont(None,80) #25 é o tamanho da mensagem
        text=fonte.render("Game Over", True, white)
        tela.blit(text,(400,400))
        pygame.display.update() 
        tempo.wait(100)
        
        
  if pygame.sprite.spritecollide(portal,bonzinho_group, True):
      malvado.vel = 0
              
  if pygame.sprite.spritecollide(portal, malvado_group, True) or  pygame.sprite.spritecollide(portal, bonzinho_group, True):
      malvado.vel = 0

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