from pygame.sprite import spritecollide, groupcollide
from classes.class_SptiteGroups import SpriteGroups

sprite_groups = SpriteGroups()

from icecream import ic

def player_guard_collision():
    object_collide = groupcollide( sprite_groups.player_guard_group, sprite_groups.enemies_shot_group, dokilla=False, dokillb=True)
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits = list(object_collide.keys())[0]
        if hits.guard_level > 0:
            hits.decrease_level(lot_hits)

        if hits.guard_level <= 0:
            hits.kill()


def enemies_guard_collision():
    object_collide = groupcollide( sprite_groups.enemies_guard_group, sprite_groups.player_shot_group, dokilla=False, dokillb=True)
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits = list(object_collide.keys())[0]
        if hits.guard_level > 0:
            hits.decrease_level(lot_hits)

        if hits.guard_level <= 0:
            hits.kill()