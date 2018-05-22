# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:42:27 2018

@author: gi_gi
"""

 # -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:03:19 2018

@author: Amanda
"""
import pygame
# ===============      CLASSES      ===============
class physics(object):
    def __init__(self):
        self.x_vel = self.y_vel = 0
        self.grav = 0.22
        self.fall = False

    def physics_update(self):
        if self.fall:
            self.y_vel += self.grav
        else:
            self.y_vel = 0

class bonequinho(physics, pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, location, speed):
        physics.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.speed = speed
        self.jump_power = -8.5
        self.rect = self.image.get_rect(topleft=location)

    def get_position(self, obstacles):
        """Calculate the player's position this frame, including collisions."""
        if not self.fall:
            self.check_falling(obstacles)
        else:
            self.fall = self.check_collisions((0,self.y_vel) , 1, obstacles)
        if self.x_vel:
            self.check_collisions((self.x_vel,0), 0, obstacles)

    def check_falling(self, obstacles):
        """If player is not contacting the ground, enter fall state."""
        self.rect.move_ip((0,1))
        if not pygame.sprite.spritecollideany(self, obstacles):
            self.fall = True
        self.rect.move_ip((0,-1))

    def check_collisions(self, offset, index, obstacles):
        """This function checks if a collision would occur after moving offset
        pixels.  If a collision is detected position is decremented by one
        pixel and retested. This continues until we find exactly how far we can
        safely move, or we decide we can't move."""
        unaltered = True
        self.rect.move_ip(offset)
        while pygame.sprite.spritecollideany(self, obstacles):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered

    def check_keys(self, keys):
        """Find the player's self.x_vel based on currently held keys."""
        self.x_vel = 0
        if keys[pygame.K_LEFT] or keys[pg.K_a]:
            self.x_vel -= self.speed
        if keys[pygame.K_RIGHT] or keys[pg.K_d]:
            self.x_vel += self.speed

    def jump(self):
        """Called when the user presses the jump button."""
        if not self.fall:
            self.y_vel = self.jump_power
            self.fall = True

    def update(self, obstacles, keys):
        """Everything we need to stay updated."""
        self.check_keys(keys)
        self.get_position(obstacles)
        self.physics_update()

    def draw(self,surface):
        """Blit the player to the target surface."""
        surface.blit(self.image, self.rect)


        
