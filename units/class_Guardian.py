from pygame.sprite import Sprite
from classes.class_Animator import Animator

from functions.function_guards_collision import player_guard_collision, enemies_guard_collision


class Guadrian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=0.05,
        obj_rect=None,
        guard_level=None,
        loops=-1,
        obj=None
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            obj_rect=obj_rect,
            loops=loops,
            obj=obj
            )

        self.guard_level = guard_level

    def decrease_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value

    
    def update(self):
        player_guard_collision()
        enemies_guard_collision()
        super().update()