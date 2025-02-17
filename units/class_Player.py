from pygame.sprite import Sprite
from pygame.transform import rotozoom
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_w, K_d, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

from config.create_Objects import screen
from config.sources.heroes.source import HEROES
from units.class_Shoots import Shoots
from units.class_Guardian import Guadrian
from logic.class_DeltaTime import DeltaTime


from classes.class_SptiteGroups import SpriteGroups

from functions.function_player_collision import player_collision



class Player(Sprite):
    def __init__(
        self,
        pos=None,
    ):
        self.sptite_groups = SpriteGroups()
        super().__init__(self.sptite_groups.camera_group)
        self.sptite_groups.camera_group.add(self)
        self.sptite_groups.player_group.add(self)

        self.pos = pos
        self.direction = Vector2(pos)
        self.angle = 0
        self.first_shot = False
        self.__post_init__()

    def __post_init__(self):
        self.image_rotation = HEROES[1]["angle"][0]["sprite"]
        self.rect = self.image_rotation.get_rect(center=self.pos)

        self.speed = HEROES[1]["speed"]
        self.rotation_speed = HEROES[1]["rotation_speed"]

        self.shield = Guadrian(
            dir_path="images/Guards/guard1",
            speed_frame=0.09,
            obj_rect=self.rect,
            guard_level=10,
            loops=-1
        )

        self.prepare_weapons(0)

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == -1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()

            elif event.y == 1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.first_shot = not self.first_shot
                self.shoot()

    def prepare_weapons(self, angle):
        self.pos_weapons = []
        for value in HEROES[1]["angle"][angle]["weapons"]:
            self.pos_weapons.append(value)

    def shoot(self):
        for value in self.pos_weapons_rotation:
            self.sptite_groups.camera_group.add(
                shot := Shoots(
                    pos=(value),
                    speed=12,
                    angle=self.angle,
                    shoter=self,
                    kill_shot_distance=2000,
                    image="images/Rockets/shot3.png",
                    scale_value=0.2,
                )
            )
            self.sptite_groups.player_shot_group.add(shot)

    @property
    def pos_weapons_rotation(self):
        result = []
        for weapon in self.pos_weapons:
            x, y = weapon
            newX, newY = self.vector_rotation([x, y], -self.angle / 57.5)
            result.append([self.rect.centerx + newX, self.rect.centery + newY])
        return result

    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)

    def rotation(self):
        for value in HEROES[1]["angle"]:
            if self.angle <= value:
                self.image = HEROES[1]["angle"][value]["sprite"]
                self.prepare_weapons(value)
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        if self.rect.left <= self.sptite_groups.camera_group.background_rect.left:
            self.rect.left = self.sptite_groups.camera_group.background_rect.left
        if self.rect.right >= self.sptite_groups.camera_group.background_rect.right:
            self.rect.right = self.sptite_groups.camera_groupbackground_rect.right
        if self.rect.top <= self.sptite_groups.camera_group.background_rect.top:
            self.rect.top = self.sptite_groups.camera_group.background_rect.top
        if self.rect.bottom >= self.sptite_groups.camera_group.background_rect.bottom:
            self.rect.bottom = self.sptite_groups.camera_group.background_rect.bottom

    def move(self):
        keys = get_pressed()
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)

    def update(self):
        self.check_position()
        self.move()
        self.shield.animate(self.rect)

        # player_collision(self)

        # if hasattr(self, 'expl_enemies_rocket'):
        #     if self.expl_enemies_rocket.loops > 0:
        #         self.expl_enemies_rocket.animate(self.rect)
        #     # else:
            #     delattr(self, 'expl_enemies_rocket')


        for value in self.pos_weapons_rotation:
            value[0] += self.direction.x
            value[1] += self.direction.y
