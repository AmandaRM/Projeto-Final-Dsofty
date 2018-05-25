import pygame
import sys
from pygame.locals import *
from random import randrange
import plataform
import movimento
import username


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
seg=0
minu=0
gameover=False
# ===============   LOOPING PRINCIPAL   ===============

rodando = True
relogio=pygame.time.Clock()
inicio_jogo= True

while rodando:
  tempo=relogio.tick(30)
  cont+=1
  if gameover == False:
      if cont%30 == 0:
          seg+=1
          if seg == 59:
              minu+=1
              seg=0
          
  if inicio_jogo:
          tela2 = pygame.display.set_mode((800, 600), 0, 32)
          pygame.display.set_caption('Star Lego')
          fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
          iniciar_jogo = movimento.bonequinho("start_game.png", 195, 300)
          iniciar_jogo_group=pygame.sprite.Group()
          iniciar_jogo_group.add(iniciar_jogo)
          nome_jogo= movimento.bonequinho("starlego.png", 125, 180)
          nome_jogo_group=pygame.sprite.Group()
          nome_jogo_group.add(nome_jogo)
          tela2.blit(fundo, (0, 0))
          nome_jogo_group.draw(tela2)
          iniciar_jogo_group.draw(tela2)
          nome_usuario.blit(tela2)
          
          for event in pygame.event.get():
          
              if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                 rodando = False 
             
              tecla_pressionada = pygame.key.get_pressed()
              if tecla_pressionada[K_RETURN]:
                  inicio_jogo=False
          pygame.display.update()      
      
  if inicio_jogo==False:   
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
         text2=fonte.render(str(seg) , True, white)
         text3=fonte.render(str(minu), True, white)
         text4=fonte.render(":", True, white)
         tela.blit(text, (700,20)) 
         tela.blit(text2, (780,20)) 
         tela.blit(text3,(760, 20))
         tela.blit(text4, (770, 20))
         
         pygame.display.update() 
    
         portal=movimento.bonequinho("portal.png", 0,0)
         #portal=pygame.transform.rotate(, 90)=================================
         portal_group= pygame.sprite.Group()
         portal_group.add(portal)
    
           
    
         for event in pygame.event.get():     #pega lista de eventos 0)
             if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                rodando = False            #executa a função de sistema "exit"
             if event.type == pygame.KEYDOWN:
                 if event.key == K_UP:
                     if pygame.sprite.spritecollide(bonzinho, Plataforma, False) or pygame.sprite.spritecollide(bonzinho, chao_group, False) or pygame.sprite.spritecollide(bonzinho,Plataformas_Vermelhas, True) or pygame.sprite.spritecollide(bonzinho, Plataformas_Amarelas, False):
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
##                    
#          def collide(self, x, y, plataform):
#               if pygame.sprite.collide_rect(self, plataform.rect):
#                   if  xvel > 0:
#                       self.rect.right = plataform.rect.left
#                   if xvel< 0 :
#                       self.rect.left = plataform.rect.right
#                   if yvel > 0:
#                       self.rect.bottom=plataform.rect.top
#                       self.onGround=True 
#                       self.yvel=0
#                   if yvel<0:
#                       self.rect.top = plataform.rect.bottom
                       
                       
#               for e in :
#                if pygame.sprite.collide_rect(bonzinho, e.rect):
#                   if  bonzinho.rect.x  > 0:
#                       bonzinho.rect.right = e.rect.left
#                       bonzinho.vel=0
#                   if bonzinho.rect.x < 0 :
#                       bonzinho.rect.left = e.rect.right
#                       bonzinho.vel=0
#                   if bonzinho.rect.y > 0:
#                       bonzinho.rect.bottom= e.rect.top
#                       bonzinho.onGround=True 
#                       bonzinho.vel=0
#                   if bonzinho.rect.y < 0:
#                       bonzinho.rect.top = e.rect.bottom
#                       bonzinho.vel=0
                       
                       
               
            
#          if pygame.sprite.spritecollide(Plataf, portal_group, True):
#              continue

#          if pygame.sprite.spritecollide(Plataf, portal_group, True):
#              continue
                    
    
         for e in Plataformas_Vermelhas:
             e=plataform.move_plataforma(e, 400, 200)
    
         listaColididos = pygame.sprite.spritecollide(bonzinho, Plataforma, False)
         if listaColididos:
             if listaColididos[0].rect.top > bonzinho.rect.top:
                 bonzinho.vel = 0
                 bonzinho.rect.bottom=listaColididos[0].rect.top
             if listaColididos[0].rect.bottom > bonzinho.rect.top:
                 bonzinho.vel=3
             
         condicao=True
         lista = pygame.sprite.spritecollide(bonzinho, Plataformas_Verdes, condicao) #collide só para o pé do bicho
         if lista:
             if lista[0].rect.bottom > bonzinho.rect.top:
                 condicao=False
                 bonzinho.vel=3
             else:
                 condicao=True
             
         lista2 = pygame.sprite.spritecollide(bonzinho, Plataformas_Amarelas, False)
         if lista2:
             if lista2[0].rect.top <= bonzinho.rect.bottom:
                 bonzinho.vel=-3

             if lista2[0].rect.bottom > bonzinho.rect.top:
                 bonzinho.vel = 3
           
       
         lista3 = pygame.sprite.spritecollide(bonzinho,Plataformas_Vermelhas, False)
         if lista3:
             if lista3[0].rect.bottom > bonzinho.rect.top:
                bonzinho.vel=0
           
             
         lista5 = pygame.sprite.spritecollide(malvado, Plataforma, False)
         if lista5:
             if lista5[0].rect.top > malvado.rect.top:
                 malvado.vel = 0
                 malvado.rect.bottom=lista5[0].rect.top
             if lista5[0].rect.bottom > malvado.rect.top:
                 malvado.vel = 3
             
         lista4 = pygame.sprite.spritecollide(bonzinho, chao_group, False)
         if lista4:
             if lista4[0].rect.top > bonzinho.rect.top:
                 bonzinho.rect.bottom=lista4[0].rect.top+1
                 bonzinho.vel = 0
             
         if pygame.sprite.spritecollide(malvado, chao_group, False):
             malvado.vel = 0
             
         if pygame.sprite.spritecollide(malvado, bonzinho_group, True):
               fonte=pygame.font.SysFont(None,80) #25 é o tamanho da mensagem
               text=fonte.render("Game Over", True, white) 
               tela.blit(text,(400,400))
               gameover=True
               pygame.display.update() 

               
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
        
         elif pressed_keys[K_a]:
              malvado=movimento.bonequinho.bom_LEFT(malvado)
         elif pressed_keys[K_d]:
              malvado=movimento.bonequinho.bom_RIGHT(malvado)  
#        
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
         bonzinho.vel+=2.5
     
         malvado.rect.y+=malvado.vel
         malvado.vel+=2.5
          
cont+=1  
#menu.game_menu()
pygame.display.quit()