import pygame as pg
from pygame.sprite import Sprite
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, K_a, K_w, K_d, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

import math
from random import uniform, randint, choice

from units.class_Shoots import Shoots

from sources.enemies.source import ENEMIES


class Enemies(Sprite):
    def __init__(self,
                group=None,
                player=None):
        super().__init__(group)
        
        self.group = group
        self.angle = 0
        self.speed = randint(0, 10)
        self.direction_list = [0, 1, -1]
        self.moce_counter = randint(0, 600)
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)
        self.player = player
        self.shots = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.__post_init__()
        self.group.add(self)

    def __post_init__(self):
        self.image_rotation = ENEMIES[1]['angle'][0]['sprite']

        self.pos = (
                    uniform(
                            self.group.background_rect.left + 200,
                            self.group.background_rect.right - 200
                            ),
                    uniform(
                            self.group.background_rect.top + 200,
                            self.group.background_rect.bottom - 200
                            )
                    )
        
        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)


    def rotate_vector(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)


    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMIES[1]['angle']:
            if self.angle <= value:
                self.image = ENEMIES[1]['angle'][value]['sprite']
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        if self.rect.left <= self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
        if self.rect.right >= self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
        if self.rect.top <= self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
        if self.rect.bottom >= self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom

    def move(self):
        pass
    
    def shoot(self):
        self.group.add(Shoots(pos=self.rect.center,
                            player=self.player,
                            group=self.group,
                            speed=7,
                            angle=self.angle,
                            kill_shot_distance=2000))
    
    
    def update(self):
        self.check_position()
        self.rotation()
        self.move()
        # if randint(0, 100) == 50:
        #     self.shoot()


