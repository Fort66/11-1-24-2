from pygame.sprite import Sprite
from pygame.transform import rotozoom
from pygame.math import Vector2

import math
from random import (
    uniform,
    randint,
    choice
    )
from time import time

from units.class_Shoots import Shoots
from units.class_Guardian import Guadrian

from config.create_Objects import (
    checks,
    weapons
    )
# from config.sources.enemies.source import ENEMIES

from classes.class_SptiteGroups import SpriteGroups

from functions.function_enemies_collision import enemies_collision
from functions.function_load_source import load_python_file_source

ENEMY = load_python_file_source(
    dir_path='config.sources.enemies',
    module_name='source',
    level=1,
    name_source='ENEMY'
)


class Enemies(Sprite):
    def __init__(self, player=None):
        self.sptite_groups = SpriteGroups()
        super().__init__(self.sptite_groups.camera_group)
        self.sptite_groups.enemies_group.add(self)

        self.angle = 0
        self.player = player
        self.min_distance = ENEMY['min_distance']
        self.shot_distance = ENEMY['shot_distance']
        self.is_min_distance = False
        self.shot_time = 0
        self.hp = ENEMY['hp']
        self.random_value()
        self.change_direction()
        self.__post_init__()

    def __post_init__(self):
        self.image = ENEMY["angle"][0]["sprite"]
        self.image_rotation = self.image.copy()

        self.pos = (
            uniform(
                self.sptite_groups.camera_group.background_rect.left + self.image.get_width(),
                self.sptite_groups.camera_group.background_rect.right - self.image.get_width(),
            ),
            uniform(
                self.sptite_groups.camera_group.background_rect.top + self.image.get_height(),
                self.sptite_groups.camera_group.background_rect.bottom - self.image.get_height(),
            ),
        )

        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)

        self.sptite_groups.camera_group.add(
            shield := Guadrian(
                dir_path="images/Guards/guard2",
                speed_frame=0.09,
                guard_level=randint(3, 10),
                loops=-1,
                angle=self.angle,
                scale_value=(1, 1),
                size=self.rect.size,
                owner=self
            )
        )
        self.sptite_groups.enemies_guard_group.add(shield)
        self.prepare_weapons(0)

    def prepare_weapons(self, angle):
        weapons.load_weapons(
            obj=self,
            source=ENEMY["angle"][angle]["weapons"],
            angle=angle,
        )

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(obj=self, angle=self.angle)

    def random_value(self):
        self.speed = randint(ENEMY['speed'][0], ENEMY['speed'][1])
        self.direction_list = ENEMY['direction_list']
        self.move_counter = uniform(ENEMY['move_counter'][0], ENEMY['move_counter'][1])
        self.move_time = time()
        self.permission_shot = uniform(ENEMY['permission_shot'][0], ENEMY['permission_shot'][1])

    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)

    def check_move_count(self):
        if time() - self.move_time >= self.move_counter:
            self.random_value()
            self.change_direction()

    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMY["angle"]:
            if self.angle <= value:
                self.image = ENEMY["angle"][value]["sprite"]
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        checks.position(self, self.sptite_groups.camera_group.background_rect)
        if not checks.resolved_move:
            self.change_direction()

        if not self.is_min_distance:
            if (
                Vector2(self.rect.center).distance_to(self.player.rect.center)
                <= self.min_distance
            ):
                self.is_min_distance = True
                # self.random_value()
                self.change_direction()

        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            > self.min_distance
        ):
            self.is_min_distance = False

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)

    def shot(self):
        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            <= self.shot_distance
        ):
            if self.player.first_shot:
                if self.shot_time == 0:
                    self.shot_time = time()
                if time() - self.shot_time >= self.permission_shot:
                    value = self.pos_weapons_rotation()
                    for pos in value:
                        self.sptite_groups.camera_group.add(
                            shot := Shoots(
                                pos=(pos),
                                speed=8,
                                angle=self.angle,
                                kill_shot_distance=2000,
                                image="images/Rockets/shot1.png",
                                scale_value=0.09,
                                owner=self
                            )
                        )
                        self.sptite_groups.enemies_shot_group.add(shot)
                        self.shot_time = time()

    def decrease_hp(self, value):
        if self.hp > 0:
            self.hp -= value
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.shot()
        enemies_collision()
        weapons.update_weapons(self, self.angle)
