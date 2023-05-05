
import random

import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import DEFAULT_TYPE, SMALL_HEART, SMALL_HEART_TYPE


class SmallHeart(PowerUp):
    SMALL_HEART_HEIGHTS = [250, 290, 320]
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        super().__init__(SMALL_HEART, SMALL_HEART_TYPE) 
        self.rect.y = random.choice(self.SMALL_HEART_HEIGHTS)

      