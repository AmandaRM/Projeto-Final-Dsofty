# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:52:20 2018

@author: Amanda
"""
import pygame
import random

class Plataform (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, dimension):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = dimension[0]
        self.rect.y = dimension[1]
        

#def cria_Plataform_Aleatoria():
#    plataformas_group=pygame.sprite.Group()
#    x=random.randint(130,200)
#    y=random.randint(50,100)
#    plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y]) 
#    if 0<plataforma1.rect.x<128 and 0<plataforma1.rect.y<128:  
#        x=random.randint(130,200)
#        y=random.randint(20,200)
#        plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])
#    plataformas_group.add(plataforma1)
#    contador = 0
#    while contador < 2:
#        delta_x=random.randint(50,100)
#        delta_y =random.randint(100,200)
#        plataforma2=Plataform("plataform_de_pedra_reta_pequena.png", [plataforma1.rect.x, plataforma1.rect.y])
#        plataforma2.rect.x += delta_x
#        plataforma2.rect.y += delta_y
#        plataformas_group.add(plataforma2)
#        contador +=1
#    
#        
#       return() 
def cria_Plataform_Aleatoria():
    plataformas_group=pygame.sprite.Group()
    i=0
    x=[]
    x.append(random.randint(0,200))
    x.append(random.randint(250,400))
    x.append(random.randint(450,600))
    x.append(random.randint(650,700))
    y=[]
    y.append(random.randint(50,170))
    y.append(random.randint(220,270))
    y.append(random.randint(320,370))
    y.append(random.randint(420,470))
    while i<4:
        plataforma=Plataform("plataform_de_pedra_reta_pequena.png", [x[0], y[i]])
        plataformas_group.add(plataforma)
        
        plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x[1], y[i]])
        plataformas_group.add(plataforma1)
        
        plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x[2], y[i]])
        plataformas_group.add(plataforma1)
        
        plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x[3], y[i]])
        plataformas_group.add(plataforma1)
        i+=1
    return plataformas_group

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    


"""    i=0
    plataformas_group=pygame.sprite.Group()
    while i<15:
        x=50
        y=100
        if i<=4:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)
        #x=100
        #y=200
        elif i<=7:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)
        #x=50
        #y=300
        elif i<=12:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)
        #x=100
        #y=400
        elif i<=15:
            x+=50
            plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [x, y])        
            plataformas_group.add(plataforma1)        
        i+=1
    return plataformas_group
    """
def cria_Plataform_nAleatoria():
     plataformas_group=pygame.sprite.Group()
     plataforma1=Plataform("plataform_de_pedra_reta_pequena.png", [50, 400])        
     plataformas_group.add(plataforma1)
     plataforma2=Plataform("plataform_de_pedra_reta_pequena.png", [150, 100])        
     plataformas_group.add(plataforma2)
     plataforma3=Plataform("plataform_de_pedra_reta_pequena.png", [250, 400])        
     plataformas_group.add(plataforma3)
     plataforma4=Plataform("plataform_de_pedra_reta_pequena.png", [350, 100])        
     plataformas_group.add(plataforma4)
     plataforma5=Plataform("plataform_de_pedra_reta_pequena.png", [450, 400])        
     plataformas_group.add(plataforma5)
     plataforma6=Plataform("plataform_de_pedra_reta_pequena.png", [650, 400])        
     plataformas_group.add(plataforma6)
     plataforma7=Plataform("plataform_de_pedra_reta_pequena.png", [550, 100])        
     plataformas_group.add(plataforma7)
     
     plataforma8=Plataform("plataform_de_pedra_reta_pequena.png", [50, 200])        
     plataformas_group.add(plataforma8)
     plataforma9=Plataform("plataform_de_pedra_reta_pequena.png", [150, 300])        
     plataformas_group.add(plataforma9)
     plataforma10=Plataform("plataform_de_pedra_reta_pequena.png", [250, 200])        
     plataformas_group.add(plataforma10)
     plataforma11=Plataform("plataform_de_pedra_reta_pequena.png", [350, 300])        
     plataformas_group.add(plataforma11)
     plataforma12=Plataform("plataform_de_pedra_reta_pequena.png", [450, 200])        
     plataformas_group.add(plataforma12)
     plataforma13=Plataform("plataform_de_pedra_reta_pequena.png", [650, 200])        
     plataformas_group.add(plataforma13)
     plataforma14=Plataform("plataform_de_pedra_reta_pequena.png", [550, 300])        
     plataformas_group.add(plataforma14)
     
     plataforma15=Plataform("plataform_de_pedra_reta_pequena.png", [150, 500])        
     plataformas_group.add(plataforma15)
     plataforma16=Plataform("plataform_de_pedra_reta_pequena.png", [350, 500])        
     plataformas_group.add(plataforma16)
     plataforma17=Plataform("plataform_de_pedra_reta_pequena.png", [550, 500])        
     plataformas_group.add(plataforma17)
     return plataformas_group
