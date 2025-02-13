import pygame as pg
from pygame.locals import *



class CheckEvents:
     def __init__(self, game: object = None):
         self.game: object = game
         self.angle: int = 0
         

     def check_events(self):

        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.game.run = False


            # if event.type == MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         self.game.player.shots()
            
            self.game.player.handle_event(event)
            
            # if event.type == MOUSEWHEEL:
            #     if event.y == 1:
            #         self.angle = -10
            #         self.game.player.rotate(self.angle)

            #     if event.y == -1:
            #         self.angle = 10
            #         self.game.player.rotate(self.angle)

