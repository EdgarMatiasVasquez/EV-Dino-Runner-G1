import pygame
from dino_runner.components.dinosaur import Dinosaur

from dino_runner.utils.constants import DEFAULT_TYPE, HAMMER_TYPE

class Score:
    def __init__(self):
        self.score = 0
        self.max_score = 0
        self.player = Dinosaur()
       
    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2
        elif self.score > self.max_score:
            self.max_score = self.score   
    def draw(self, show_message):
        show_message(center_x=1000, center_y=25,letter_size=18, message=f"Score: {self.score}", color=(0, 0, 0))
        show_message(center_x=1000, center_y=50, letter_size=12, message=f"Max  Score: {self.max_score}",color=(64, 64, 64))
    def reset(self):
        self.score = 0


    