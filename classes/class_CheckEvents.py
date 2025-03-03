import pygame as pg
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    VIDEORESIZE
    )


class CheckEvents:
    def __init__(self, game: object = None):
        self.game: object = game
        self.angle: int = 0

    def check_events(self):

        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.game.run = False

            if event.type == VIDEORESIZE:
                self.game.screen.rect = self.game.screen.window.get_rect()

            self.game.player.handle_event(event)
