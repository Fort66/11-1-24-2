from pygame.image import load
from pygame.transform import scale
from classes.class_SptiteGroups import SpriteGroups

from os import listdir
from time import time
import numpy as np

from icecream import ic


class Animator:
    def __init__(
                self,
                dir_path=None,
                speed_frame=.05,
                obj=None,
                obj_rect=None,
                loops=-1
                ):
        self.sptite_groups = SpriteGroups()
        super().__init__(self.sptite_groups.camera_group)

        self.dir_path = dir_path
        self.speed_frame = speed_frame
        self.obj = obj
        self.obj_rect = obj_rect

        self.frames = 0
        self.frame = 0
        self.frame_time = 0
        self.loops = loops
        self.paused = False
        self.__post_init__()


    def __post_init__(self):
        self.file_list = sorted(listdir(self.dir_path))
        self.original_frames = np.array([[scale(load(f'{self.dir_path}/{value}').convert_alpha(), self.obj_rect[2:]), self.speed_frame] for value in self.file_list])
        self.frames = self.original_frames.copy()
        self.image_rotation = self.frames[self.frame][0]
        self.rect = self.image_rotation.get_rect(center=self.obj_rect.center)


    def update(self):
        self.obj_rect = self.obj.rect

        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time > self.frames[self.frame][1]:
            if self.loops == -1:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
                self.frame_time = time()

            if self.loops > 0:
                if self.frame < len(self.frames) - 1:
                    self.frame = self.frame + 1
                    self.frame_time = time()
                if self.frame == len(self.frames) - 1:
                    self.loops -= 1


            if self.loops:
                self.frames[self.frame][0] = self.original_frames[self.frame][0].copy()
                self.frames[self.frame][0] = scale(self.frames[self.frame][0], self.obj_rect[2:])

        self.image_rotation = self.frames[self.frame][0]
        self.rect = self.image_rotation.get_rect(center=self.obj_rect.center)






