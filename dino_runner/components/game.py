from tkinter import font
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, DINO_DEAD, DINO_START, GAME_OVER, HAMMER_TYPE, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacleManager = ObstacleManager()
        self.score = Score()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.speed_hammer = 0
    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.quit()
    def play(self):
        # Game loop: events - update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.playing = True
        self.score.reset()
        self.game_speed = 20
        self.obstacleManager.reset()
        self.power_up_manager.reset()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacleManager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_power_up( self.show_message, self.game_speed, self)
        self.obstacleManager.draw(self.screen)
        self.score.draw(self.show_message)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def on_death(self): 
        is_invincible = self.player.type == SHIELD_TYPE
        is_destructor = self.player.type == HAMMER_TYPE
        if is_destructor:
            self.obstacleManager.obstacles = []
            self.game_speed -= 4
        elif not is_invincible and not is_destructor: 
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1

    def show_menu(self):  
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        CENTER_Y_SCORE = center_y +150
        CENTER_Y_DEATH_COUNT = center_y +150
        CENTER_Y_MAX_SCORE = center_y +150
        #self.screen.fill((255, 255, 255))
        if self.death_count == 0:
            self.screen.fill((192, 192, 192))
            self.show_message(center_x, center_y, letter_size=30, message="Press any key to start", color=(0,0,0))
            self.screen.blit(DINO_START,(center_x -49, center_y -121))
        else:
            self.screen.fill((32, 32, 32))
            self.show_message(center_x, center_y-150,letter_size=50, message="GAME OVER", color=(204, 0, 0))
            self.show_message(center_x, center_y+30,letter_size=15, message="Press any key to Restart", color=(224, 224, 224)) 
            self.show_message(center_x, center_y=CENTER_Y_SCORE, letter_size=35, message=f"Your Score: {self.score.score}", color=(0, 255, 255))
            self.show_message(center_x-290, center_y=CENTER_Y_DEATH_COUNT, letter_size=30, message=f" Death Count: {self.death_count}", color=(0, 153, 153))
            self.show_message(center_x+290, center_y=CENTER_Y_MAX_SCORE, letter_size=30, message=f"Max Score: {self.score.max_score}",color=(0, 153, 153))
            self.screen.blit(RESET,(center_x -49,center_y -60))
            
        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()
            

    def show_message(self, center_x, center_y, letter_size, message, color):
        font = pygame.font.Font('freesansbold.ttf', letter_size)
        text = font.render(message, True, (color))
        text_rect = text.get_rect()
        text_rect.center = (center_x, center_y)
        self.screen.blit(text, text_rect)

                          