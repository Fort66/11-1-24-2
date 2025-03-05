from pygame.transform import rotozoom
from pygame.sprite import Sprite

from time import time

from classes.class_Animator import Animator

from functions.function_guards_collision import (
    player_guard_collision,
    enemies_guard_collision,
    guards_collision
    )
from functions.function_load_source import load_json_source


class Guadrian(Animator, Sprite):
    def __init__(
        self,
        types=None,
        dir_path=None,
        speed_frame=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        size=None,
        angle=None,
        owner=None
    ):
        if types:
            self.source = load_json_source(
                dir_path='config/sources/guards',
                level=types
            )
            self.dir_path = self.source['dir_path']
            self.speed_frame = self.source['speed_frame']
            self.guard_level = self.source['guard_level']
            self.scale_value = self.source['scale_value']
            self.loops = self.source['loops']
        else:
            self.dir_path = dir_path
            self.speed_frame = speed_frame
            self.guard_level = guard_level
            self.scale_value = scale_value
            self.loops = loops

        super().__init__(
            dir_path=self.dir_path,
            speed_frame=self.speed_frame,
            loops=self.loops,
            size=size,
            scale_value=self.scale_value
            )

        # self.guard_level = guard_level
        self.angle = angle
        self.destruction_time = 0
        self.owner = owner
        self.rect = self.image_rotation.get_rect(center=self.owner.rect.center)

    def decrease_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value


    def update(self):
        player_guard_collision()
        enemies_guard_collision()
        self.angle = self.owner.angle
        self.rect.center = self.owner.rect.center
        self.image_rotation = self.frames[self.frame][0]
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)
        super().animate()

        if guards_collision():
            if self.destruction_time <= 0:
                self.destruction_time = time()