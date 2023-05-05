import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DINO_DEAD, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER, HAMMER_TYPE, JUMPING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, RUNNING_HAMMER, RUNNING_SHIELD, SCREEN_WIDTH, SHIELD_TYPE, SMALL_HEART_TYPE

JUMP_VELOCITY = 8.5
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"

RUNNING_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, SMALL_HEART_TYPE: RUNNING  }
JUMPING_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, SMALL_HEART_TYPE: JUMPING}
DUCKING_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, SMALL_HEART_TYPE: DUCKING}


class Dinosaur(Sprite): #PasCalCase
    POS_Y = 310 
    POS_X = 80
    POS_Y_DUCK = 340
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUNNING_IMG[self.type][0]
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

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING
        
        if self.step >=10:
           self.step = 0

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def run(self):
        self.rect.y = self.POS_Y
        self.image = RUNNING_IMG[self.type][0] if self.step < 5 else RUNNING_IMG[self.type][1]
        self.step += 1

    def jump(self):
        pos_y = self.rect.y - self.jump_velocity * 4
        self.image = JUMPING_IMG[self.type]
        self.jump_velocity -= 0.8
        self.rect.y = pos_y
        if self.jump_velocity < -JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.action = DINO_RUNNING
            self.jump_velocity = JUMP_VELOCITY

    def duck(self):
        self.rect.y = self.POS_Y_DUCK
        self.image = DUCKING_IMG[self.type][0] if self.step < 5 else DUCKING_IMG[self.type][1] 
        self.step += 1
    def on_pick_power_up(self, power_up, on_death_small_heart):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
        if self.type == SMALL_HEART_TYPE:
            on_death_small_heart()

    def draw_power_up(self, show_message, game_speed, game):
        if self.type == SHIELD_TYPE or self.type ==HAMMER_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show <= 1 and time_to_show >= 0 :
                show_message(center_x=SCREEN_WIDTH // 2, center_y=50 // 2,letter_size=22, message=f"{self.type.capitalize()} enabled for {time_to_show}", color=(255, 0, 0))
            elif time_to_show >= 0:
                show_message(center_x=SCREEN_WIDTH // 2, center_y=50 // 2,letter_size=22, message=f"{self.type.capitalize()} enabled for {time_to_show}", color=(0, 0, 0))  
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0
        if self.type == SMALL_HEART_TYPE:
            time_to_show = 0



        
    
        
            
 



