import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING
JUMP_VELOCITY = 8.5
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"



class Dinosaur(Sprite): #PasCalCase
    POS_Y = 310 
    POS_X = 80
    POS_Y_DUCK = 340
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = JUMP_VELOCITY

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()

        elif self.action == DINO_JUMPING:
           self.jump()

        elif self.action == DINO_DUCKING:
           self.duck()

        if user_input[pygame.K_UP] and self.action != DINO_JUMPING:
             self.action = DINO_JUMPING

        elif user_input[pygame.K_DOWN] and self.action != DINO_JUMPING:
            self.action = DINO_DUCKING
        elif not (self.action == DINO_JUMPING or user_input[pygame.K_DOWN]):
            self.action = DINO_RUNNING
        
        if self.step >=10:
           self.step = 0

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.action = DINO_RUNNING
            self.jump_velocity = JUMP_VELOCITY

    def duck(self):
        self.rect.y = self.POS_Y_DUCK
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.step += 1
        
            
 


