import random
from dino_runner.components.obstacles.obstacles import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.step = 0

    def draw(self, screen):
        if self.step >=10:
           self.step = 0
        screen.blit(self.image[0] if self.step < 5 else self.image[1], self.rect)
        self.step += 1
