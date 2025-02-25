from pygame.transform import rotozoom
from pygame.sprite import Sprite
from classes.class_Animator import Animator

from time import time

from functions.function_guards_collision import player_guard_collision, enemies_guard_collision, guards_collision


class Guadrian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        guard_level=None,
        loops=-1,
        size=None,
        angle=None,
        scale_value=None
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            loops=loops,
            size=size,
            scale_value=scale_value
            )

        self.guard_level = guard_level
        self.angle = angle
        self.obj = obj
        self.destruction_time = 0

    def decrease_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value


    def update(self):
        player_guard_collision()
        enemies_guard_collision()
        self.angle = self.obj.angle
        self.rect.center = self.obj.rect.center
        self.image_rotation = self.frames[self.frame][0]
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)
        super().animate()

        if guards_collision():
            if self.destruction_time <= 0:
                self.destruction_time = time()