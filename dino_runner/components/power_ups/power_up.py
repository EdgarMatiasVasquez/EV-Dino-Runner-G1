import random
import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SMALL_HEART_TYPE
class PowerUp:
    def __init__(self, image: pygame.Surface, power_up_type): 
        self.type = power_up_type
        self.image = image
        self.rect =self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        
        self.start_time = 0
        self.duration = random.randint(3, 5)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen, show_message ):
        screen.blit(self.image, self.rect)
        if self.type == SMALL_HEART_TYPE:
            show_message(center_x=SCREEN_WIDTH // 2, center_y=50 ,letter_size=20, message="Take care of SMALL HEART", color=(204, 0, 0))
            show_message(center_x=SCREEN_WIDTH // 2, center_y=100 ,letter_size=30, message="↓", color=(204, 0, 0))
            screen.blit(self.image, self.rect)