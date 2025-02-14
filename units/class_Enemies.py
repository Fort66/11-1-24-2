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
from units.class_Guardian import Guadrian

from config.sources.enemies.source import ENEMIES


class Enemies(Sprite):
    def __init__(self,
                group=None,
                player=None):
        super().__init__(group)

        self.group = group
        self.angle = 0
        self.random_value()
        self.change_direction()
        self.player = player
        self.min_distance = 300
        self.shot_distance = 1500
        self.is_min_distance = False
        self.__post_init__()
        self.group.add(self)

    def __post_init__(self):
        self.image = ENEMIES[1]['angle'][0]['sprite']
        self.image_rotation = self.image.copy()

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
        
        self.shield = Guadrian(
                                dir_path='images/Guards/guard2',
                                speed_frame=.09,
                                obj_rect=self.rect
                                )
        


    def random_value(self):
        self.speed = randint(0, 10)
        self.direction_list = [0, 1, -1]
        self.move_counter = randint(0, 600)


    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)


    def check_move_count(self):
        if self.move_counter <= 0:
            self.random_value()
            self.change_direction()
        else:
            self.move_counter -= 1


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
            self.change_direction()
        if self.rect.right >= self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
            self.change_direction()
        if self.rect.top <= self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
            self.change_direction()
        if self.rect.bottom >= self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom
            self.change_direction()

        if not self.is_min_distance:
            if Vector2(self.rect.center).distance_to(self.player.rect.center) <= self.min_distance:
                self.is_min_distance = True
                self.random_value()
                self.change_direction()

        if Vector2(self.rect.center).distance_to(self.player.rect.center) > self.min_distance:
            self.is_min_distance = False

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)


    def shot(self):
        if Vector2(self.rect.center).distance_to(self.player.rect.center) <= self.shot_distance:
            if self.player.first_shot and randint(0, 100) == 50:
                self.group.add(
                                Shoots(
                                        pos=self.rect.center,
                                        shoter=self,
                                        group=self.group,
                                        speed=7,
                                        angle=self.angle,
                                        kill_shot_distance=2000,
                                        image='images/Rockets/shot1.png',
                                        scale_value=.09
                                        )
                                )


    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.shot()
        self.shield.animate(self.rect)
        
        # if randint(0, 100) == 50:
        #     self.shoot()


