import pygame

class Score:
    def __init__(self):
        self.score = 0
       
    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, show_message):
        show_message(center_x=1000, center_y=50 // 2,letter_size=22, message=f"Score: {self.score}")

    def reset(self):
        self.score = 0


    