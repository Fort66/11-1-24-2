import pygame as pg
from pygame.display import (
    set_mode,
    set_caption,
    set_icon,
    get_desktop_sizes
    )
from pygame.locals import (
    RESIZABLE,
    FULLSCREEN
    )
from  pygame.image import load

from dataclasses import dataclass

pg.init()

@dataclass
class ScreenGame:
    size: tuple = (0, 0)
    color: str | tuple[int, int, int] = 'SteelBlue'
    caption: str = 'Game'
    icon: str = ''
    is_resizable: bool = False # изменяемый размер окна
    is_full_screen: bool = False # полноэкранный режим

    def __post_init__(self):
        if self.is_resizable:
            self.window = set_mode(self.size, RESIZABLE)
        elif self.is_full_screen:
            # получаем текущее разрешение экрана
            self.current_screen_resolution = get_desktop_sizes()[0]
            # print(self.current_screen_resolution)
            self.window = set_mode(self.current_screen_resolution, FULLSCREEN)
        else:
            # устанавливаем размер окна через size
            self.window = set_mode(self.size)
        # устанавливаем заголовок
        self.caption = set_caption(self.caption)
        # устанавливаем иконку
        if self.icon:
            self.icon = set_icon(load(self.icon))

        self.rect = self.window.get_rect()

    def update_caption(self, caption):
        self.caption = set_caption(caption)
