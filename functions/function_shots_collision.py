from pygame.sprite import spritecollide, groupcollide
from classes.class_SptiteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic

sprite_groups = SpriteGroups()

def player_collision():
    object_collide = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_shot_group,
        False,
        False
    ) or groupcollide(
        sprite_groups.player_group,
        sprite_groups.enemies_shot_group,
        False,
        False
    )
    if object_collide:
        hits = list(object_collide.values())[0]
        explosion = Explosion(
            dir_path='images/explosions/rocket1_expl',
            speed_frame=.01,
            scale_value=(.5, .5),
            loops=1,
            obj=hits[0],
            angle=hits[0].angle
        )
        

def enemies_collision():
    object_collide = groupcollide(
        sprite_groups.enemies_guard_group,
        sprite_groups.player_shot_group,
        False,
        False
    ) or groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        False,
        False
    )
    if object_collide:
        hits = list(object_collide.values())[0]
        explosion = Explosion(
            dir_path='images/explosions/pulsar',
            speed_frame=.01,
            scale_value=(.25, .25),
            loops=1,
            obj=hits[0],
            angle=hits[0].angle
        )


