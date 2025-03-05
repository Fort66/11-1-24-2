from pygame.sprite import groupcollide

from time import time

from classes.class_SptiteGroups import SpriteGroups

sprite_groups = SpriteGroups()


def player_guard_collision():
    object_collide = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_shot_group,
        dokilla=False,
        dokillb=True,
    )
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits_damage = list(object_collide.values())[0][0].damage
        hits = list(object_collide.keys())[0]
        if hits.guard_level > 0:
            hits.decrease_level(lot_hits * hits_damage)

        if hits.guard_level <= 0:
            hits.kill()


def enemies_guard_collision():
    object_collide = groupcollide(
        sprite_groups.enemies_guard_group,
        sprite_groups.player_shot_group,
        dokilla=False,
        dokillb=True,
    )
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits_damage = list(object_collide.values())[0][0].damage
        hits = list(object_collide.keys())[0]
        if hits.guard_level > 0:
            hits.decrease_level(lot_hits * hits_damage)

        if hits.guard_level <= 0:
            hits.kill()


def guards_collision():
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_guard_group,
        dokilla=False,
        dokillb=False,
    )

    if object_collide:
        hits_key = list(object_collide.keys())[0]
        hits_value = list(object_collide.values())[0][0]

        if time() - hits_key.destruction_time >= 1:
            if hits_key.guard_level > 0:
                hits_key.decrease_level(0.02)
        if time() - hits_value.destruction_time >= 1:
            if hits_value.guard_level > 0:
                hits_value.decrease_level(0.02)

        if hits_key.guard_level <= 0:
            hits_key.kill()

        if hits_value.guard_level <= 0:
            hits_value.kill()

    return object_collide
