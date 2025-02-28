import pygame as pg
pg.mixer.pre_init(
    44100, -16, 2, 2048
)


from config.create_Objects import screen, levels_game
from classes.class_CameraGroup import CameraGroup
from classes.class_CheckEvents import CheckEvents
from classes.class_SptiteGroups import SpriteGroups

from units.class_Player import Player
from units.class_Enemies import Enemies

from UI.Screens.class_MiniMap import MiniMap


from icecream import ic


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.screen = screen
        self.fps = 100
        self.check_events = CheckEvents(self)
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=.1, color_map=(0, 100, 0, 170))
        self.setup()

    def setup(self):
        self.player = Player(pos=screen.rect.center)

        for _ in range(levels_game.enemies_attack):
            self.sprite_groups.camera_group.add(Enemies(player=self.player))

    def  clear_player_group(self):
        self.sprite_groups.player_group.empty()
        self.sprite_groups.player_shot_group.empty()
        self.sprite_groups.player_guard_group.empty()

    def  clear_enemies_group(self):
        self.sprite_groups.enemies_group.empty()
        self.sprite_groups.enemies_shot_group.empty()
        self.sprite_groups.enemies_guard_group.empty()

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)
            self.check_events.check_events()

            if len(self.sprite_groups.enemies_group) == 0:
                self.sprite_groups.camera_group.empty()
                self.clear_player_group()
                self.clear_enemies_group()
                levels_game.attack_min += 1
                levels_game.current_level += 1
                levels_game.update_levels()
                self.sprite_groups.camera_group.set_background()
                self.setup()
            
            if len(self.sprite_groups.player_group) == 0:
                self.sprite_groups.camera_group.empty()
                self.clear_player_group()
                self.clear_enemies_group()
                levels_game.attack_min = 0
                levels_game.current_level = 1
                levels_game.update_levels()
                self.sprite_groups.camera_group.set_background()
                self.setup()
            

            self.sprite_groups.camera_group.update()
            self.sprite_groups.camera_group.custom_draw(self.player)

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
