import pygame as pg
import gif_pygame as gif

pg.mixer.pre_init(44100, -16, 2, 2048) # Инициализация звука. Инициализация плейера. (частота, биты (Если значение отрицательное, то будут использоваться подписанные значения выборки. Положительные значения означают, что будут использоваться неподписанные аудиосэмплированные выборки. Неверное значение вызывает исключение), каналы, буфер)

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


from config.create_Objects import screen
from classes.class_CameraGroup import CameraGroup
from classes.class_CheckEvents import CheckEvents
from units.class_Player import Player
from units.class_Enemies import Enemies

from icecream import ic

# space_anim = gif.GIFPygame([[pg.image.load(f'images/Backgrounds/{i}.png').convert_alpha(), .1] for i in range(10)])

# gif.transform.scale(space_anim, screen.window.get_size())

# rect_anim = space_anim.get_rect()


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        # self.delta_time = 1
        self.fps = 100
        self.win_width = screen.window.get_width()
        self.win_height = screen.window.get_height()
        self.check_events = CheckEvents(self)
        self.screen = screen
        self.create_groups()
        self.setup()


    def setup(self):
        self.player = Player(pos=screen.rect.center,
                            group=self.camera_group,)


        for _ in range(10):
            self.camera_group.add(Enemies(group=self.camera_group,
                                        player=self.player))

    def create_groups(self):
        self.camera_group = CameraGroup(self)


    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)
            # self.delta_time = self.clock.tick(self.fps) / 1000
            # space_anim.render(screen.window, rect_anim)

            # обработка игровых событий
            self.check_events.check_events()

            self.camera_group.update()
            self.camera_group.custom_draw(self.player)


            self.screen.update_caption(f'{str(round(self.clock.get_fps(), 2))}')
            pg.display.update()
            self.clock.tick()