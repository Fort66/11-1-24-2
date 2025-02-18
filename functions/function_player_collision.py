from pygame.sprite import spritecollide, groupcollide
from classes.class_SptiteGroups import SpriteGroups
from units.class_Explosion import Explosion



def player_collision(obj):
    sprite_groups = SpriteGroups()
    if len(sprite_groups.enemies_shot_group):
        hits = groupcollide(sprite_groups.enemies_shot_group, sprite_groups.player_group, dokilla=False, dokillb=False, collided=None)

        if hits:
            for hit in hits:
                obj.expl_enemies_rocket = Explosion(
                    dir_path='images/Explosions/explosion_rocket1',
                    speed_frame=.05,
                    obj_rect=obj.rect,
                    loops=1
                )
                obj.hit_rect = hit.rect

                hit.kill()

