import pygame
import sys
from pygame.locals import *
from random import randrange
import plataform
import username
import movimento
import string
from firebase import firebase 
import os
firebase=firebase.FirebaseApplication('https://projetofinal-d0c28.firebaseio.com/', None)

# ===============    MÚSICA   ===============
pygame.init()
musica = pygame.mixer.Sound("Star_lego.wav")


# ===============   INICIALIZAÇÃO   ===============
pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

# colocando o título do jogo
pygame.display.set_caption('Star Lego')

#fazendo o chão do jogo
fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()

# cria o bonzinho e criação de grupo
bonzinho = movimento.bonequinho("adventurer_stand.png",700 ,520)
bonzinho_group = pygame.sprite.Group()
bonzinho_group.add(bonzinho)
#cria o malvado e criação de grupo
malvado= movimento.bonequinho("zombie_stand.png", 200, 1)
malvado_group=pygame.sprite.Group()
malvado_group.add(malvado)

#cria o portal e criação do grupo
portal=movimento.bonequinho("portal.png", 4, 0)
portal_group = pygame.sprite.Group()
portal_group.add(portal)
portal_image=pygame.image.load("portal.png").convert()

#cria o chão e criação do grupo
chao=movimento.bonequinho("chão.png", 0, 570)
chao_group= pygame.sprite.Group()
chao_group.add(chao)

#criação da plataformas\
Plataforma, Plataformas_Amarelas, Plataformas_Vermelhas, Plataformas_Verdes =plataform.cria_Plataform_nAleatoria()

#fazer download das cores
black=(0,0,0)
white = (255, 255, 255)
yellow = (255,255,0)

#função que mostra o game over do jogo
def gameover():
    fonte=pygame.font.SysFont(None,25) #25 é o tamanho da mensagem
    text=fonte.render("Fim de jogo", True, white)
    return tela.blit(text,(400,400))
 
# formação do timer do jogo
cont=0
seg=0
minu=0
gameover=False
jogo=False
jogador=False
ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "
# ===============   LOOPING PRINCIPAL   ===============

rodando = True
relogio=pygame.time.Clock()
while rodando:

    if gameover==False:
        pygame.init()
        tela = pygame.display.set_mode((800, 600), 0, 32)
        
        # colocando o título do jogo
        pygame.display.set_caption('Star Lego')
        
        #fazendo o chão do jogo
        fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
        
        # cria o bonzinho e criação de grupo
        bonzinho = movimento.bonequinho("adventurer_stand.png",700 ,520)
        bonzinho_group = pygame.sprite.Group()
        bonzinho_group.add(bonzinho)
        #cria o malvado e criação de grupo
        malvado= movimento.bonequinho("zombie_stand.png", 200, 1)
        malvado_group=pygame.sprite.Group()
        malvado_group.add(malvado)
        
        #cria o portal e criação do grupo
        portal=movimento.bonequinho("portal.png", 4, 0)
        portal_group = pygame.sprite.Group()
        portal_group.add(portal)
        portal_image=pygame.image.load("portal.png").convert()
        
        #cria o chão e criação do grupo
        chao=movimento.bonequinho("chão.png", 0, 570)
        chao_group= pygame.sprite.Group()
        chao_group.add(chao)
    
        #criação da plataformas\
        Plataforma, Plataformas_Amarelas, Plataformas_Vermelhas, Plataformas_Verdes =plataform.cria_Plataform_nAleatoria()
    
        # formação do timer do jogo
        cont=0
        seg=0
        minu=0
        
        jogo=False
        jogador=False
        rodando2=True
        inicio_jogo=True
        name=''
        
        while rodando2:
          tempo=relogio.tick(30)
          cont+=1
 
          #fazer o relógio funcionar
          if gameover == False:
              if cont%60 == 0:
                  seg+=1
                  if seg == 59:
                      minu+=1
                      seg=0
          ############## MENU ##############        
              gambiarra = 0
              if inicio_jogo==True and jogo==False:
                      gambiarra += 1
                      if gambiarra ==1:
                          pygame.mixer.Sound.set_volume(musica, 0.3)
                          pygame.mixer.Sound.play(musica)
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
        
        
            
                      for event in pygame.event.get():                    
                          if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                             rodando = False 
                         
                          tecla_pressionada = pygame.key.get_pressed()
                          if tecla_pressionada[K_RETURN]:
                              inicio_jogo=False
                              jogador=True
                      pygame.display.update()    
                      
              if inicio_jogo==False and jogador==True:
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
                  input_box=pygame.Rect(280,300,140,32)
                  
                  
                  for event2 in pygame.event.get():
                      if event2.type == pygame.KEYDOWN:
                              if event2.key == pygame.K_RETURN:
                                 jogo=True
                                 jogador=False
                              elif event2.key == pygame.K_BACKSPACE:
                                 name = name[:-1]
                              else:
                                  name += event2.unicode
                                  print(name)
                                  print(event2.unicode)
                                                               
                                  
                                  
                  txt_surface=fonte.render(name, True, yellow)
                  width= max(200,txt_surface.get_width()+10)
                  input_box.w=width
                  tela3.blit(txt_surface, (input_box.x+5, input_box.y+5))
                  pygame.draw.rect(tela3, yellow, input_box, 2)
                  
                  pygame.display.update()            
                      
                  
                  
              
              ############## JOGO ##############    
              if jogador==False and jogo==True:
                     cont+=1
                  #desenhando o jogo na tela
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
                
                       
                # mexer nas teclas
                     for event in pygame.event.get():     #pega lista de eventos 0)
                         if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                             rodando = False            #executa a função de sistema "exit"
                         if event.type == pygame.KEYDOWN:
                             if event.key == K_UP:
                                 if pygame.sprite.spritecollide(bonzinho, Plataforma, False) or pygame.sprite.spritecollide(bonzinho, chao_group, False) or pygame.sprite.spritecollide(bonzinho,Plataformas_Vermelhas, True) or pygame.sprite.spritecollide(bonzinho, Plataformas_Amarelas, False):
                                     bonzinho=movimento.bonequinho.bom_UP(bonzinho)
                                     bonzinho.image = pygame.image.load("adventurer_jump.png")
                         if event.type == pygame.KEYUP:
                             bonzinho.image = pygame.image.load("adventurer_stand.png")
                             if event.key == K_RIGHT:
                                 bonzinho.image = pygame.image.load("adventurer_stand.png")
                         if event.type == pygame.KEYUP:
                             if event.key == K_LEFT:
                                 bonzinho.image = pygame.image.load("adventurer_stand.png")
                         if event.type == pygame.KEYUP:
                             if event.key == K_UP:
                                 bonzinho.image = pygame.image.load("adventurer_stand.png")
                                
                    
                     #===========================COLLIDE=========================================#           
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
                             malvado.rect.bottom=lista5[0].rect.top-5
                         if lista5[0].rect.bottom > malvado.rect.top:
                             malvado.vel = 10
                         
                     lista4 = pygame.sprite.spritecollide(bonzinho, chao_group, False)
                     if lista4:
                         if lista4[0].rect.top > bonzinho.rect.top:
                             bonzinho.rect.bottom=lista4[0].rect.top+1
                             bonzinho.vel = 0
                     lista6 = pygame.sprite.spritecollide(malvado, chao_group, False)    
                     if lista6:
                         if lista6[0].rect.top>malvado.rect.top:
                             malvado.rect.bottom=lista6[0].rect.top+1
                             malvado.vel = 0
                         
                     if pygame.sprite.spritecollide(malvado, bonzinho_group, True):
                           fonte=pygame.font.SysFont(None,80) #25 é o tamanho da mensagem
                           text=fonte.render("Game Over", True, white) 
                           tela.blit(text,(400,400))
                           gameover=True
                           jogo=False
                           rodando2=False
                           
                         
                     if pygame.sprite.spritecollide(portal,bonzinho_group, True):
                         malvado.vel = 0
                         gameover=True
                         jogo=False
                         rodando2=False
                                 
                     if pygame.sprite.spritecollide(portal, malvado_group, True) or  pygame.sprite.spritecollide(portal, bonzinho_group, True):
                         malvado.vel = 0
                    
                          #----------------------passar de fase---------------------
                          
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
                          
            ################### movimento do zumbi #############       
            
                     if bonzinho.rect.x > malvado.rect.x:
                          malvado=movimento.bonequinho.bom_RIGHT_light(malvado)
                          malvado.image = pygame.image.load("zombie_walk1.png")
                     if bonzinho.rect.x < malvado.rect.x:
                          malvado=movimento.bonequinho.bom_LEFT_light(malvado)
                          malvado.image = pygame.image.load("zombie_walk2.png") 
                     if bonzinho.rect.y < malvado.rect.y:
                         if pygame.sprite.spritecollide(malvado, Plataforma, False):
                             malvado=movimento.bonequinho.bom_UP_light(malvado)
                             malvado.image = pygame.image.load("zombie_jump.png") 
        
        #######ADICIONA VELOCIDADE AOS BONEQUINHOS -- COMO UMA GRAVIDADE##########
                     bonzinho.rect.y+=bonzinho.vel
                     bonzinho.vel+=2.5
             
                     malvado.rect.y+=malvado.vel
                     malvado.vel+=2.5 
            
############## GAME OVER MENU ##################
        if gameover==True and jogo==False:
            tela4 = pygame.display.set_mode((800, 600), 0, 32)
            tela4.blit(fundo, (0, 0))
                                       
            pygame.display.set_caption('Star Lego')
            fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
            restart_jogo = movimento.bonequinho("aperte_jogar.png", 195, 300) #mudar os nomes
            restart_jogo_group=pygame.sprite.Group()
            restart_jogo_group.add(restart_jogo)
            nome2_jogo= movimento.bonequinho("starlego.png", 125, 80)
            nome2_jogo_group=pygame.sprite.Group()
            nome2_jogo_group.add(nome2_jogo)
              
            fonte=pygame.font.SysFont(None,60, None)
            text0=fonte.render( "NOME: ", True, yellow)
            text02=fonte.render(str(seg) , True, yellow)
            text03=fonte.render(str(minu), True, yellow)
            text04=fonte.render("SCORE:", True, yellow)
            text05=fonte.render(str(name), True, yellow)
            text06=fonte.render(":", True, yellow)
            tela4.blit(text0, (100,240)) 
            tela4.blit(text02, (570,300)) 
            tela4.blit(text06, (550, 300))
            tela4.blit(text03,(520, 300))
            tela4.blit(text04, (500, 240))
            tela4.blit(text05, (100, 300))
            nome2_jogo_group.draw(tela4)
               #restart_jogo_group.draw(tela4)
            pygame.display.update() 
#             else:
#                tela4 = pygame.display.set_mode((800, 600), 0, 32)
#                tela4.blit(fundo, (0, 0))
#                pygame.display.set_caption('Star Lego')
#                fundo = pygame.image.load("Fundo-Estrelas.jpg").convert()
#                jogo_acabou= movimento.bonequinho("game_over.png", 300, 200)
#                jogo_acabou_group=pygame.sprite.Group()
#                jogo_acabou_group.add(jogo_acabou)
#                jogo_acabou_group.draw(tela4)
#                pygame.display.update()
                
                 

            if firebase.get('Score', None) is None:
                score={}
            else:
                score=firebase.get('Score', None)
#                
#            if gameover == True:
#                if name in score:
#                    name[minu]=minu
#                    name[seg]=seg
#                else:
#                    score[name]={}
#                    score[name]["minu"]=minu
#                    score[name]["seg"]=seg
#                              
#            firebase.patch('https://projetofinal-d0c28.firebaseio.com/', score)             
            
            fim = True
            while fim:                              
                for event in pygame.event.get():                            
                    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                        rodando = False
                        fim = False
                    if event.type == pygame.KEYDOWN:                    
                        if event.key == K_RETURN:
                            print('aa')
                            gameover=False
                            fim = False
                            
                            

 
#menu.game_menu()
pygame.display.quit()

