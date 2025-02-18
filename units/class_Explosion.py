from classes.class_Animator import Animator


class Explosion(Animator):
    def __init__(
        self, dir_path, speed_frame, obj_rect, loops
    ):
        super().__init__(dir_path, speed_frame, obj_rect, loops)