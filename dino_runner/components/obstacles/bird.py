import random
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self): 
        bird_image = BIRD[0]
        super().__init__(bird_image)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.step = 0 

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        if self.step >=10:
           self.step = 0
        self.image = BIRD [0]if self.step < 5 else BIRD[1]

        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
