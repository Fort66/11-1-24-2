from pygame.sprite import spritecollide, groupcollide
from classes.class_SptiteGroups import SpriteGroups
from units.class_Explosion import Explosion


from icecream import ic

def shots_collision(obj):
    sprite_groups = SpriteGroups()
    if obj.shoter.__class__.__name__ == 'Enemies':
        hits = spritecollide(obj, sprite_groups.player_group, dokill=False, collided=None)
        if hits:
            for hit in hits:
                obj.expl_enemies_rocket = Explosion(
                    dir_path='images/Explosions/explosion_rocket1',
                    speed_frame=.05,
                    obj_rect=hit.rect,
                    loops=1
                    )
    #         # obj.hit_rect = hit.rect
    #     # if obj.expl_enemies_rocket.loops == 0:
            obj.kill()

    if obj.shoter.__class__.__name__ == 'Player':
        hits = spritecollide(obj, sprite_groups.enemies_group, dokill=False, collided=None)
        if hits:
            obj.kill()
