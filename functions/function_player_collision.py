from pygame.sprite import spritecollide, groupcollide
from classes.class_SptiteGroups import SpriteGroups



def player_collision(obj):
    sprite_groups = SpriteGroups()
    if len(sprite_groups.enemies_shot_group):
        hits = groupcollide(sprite_groups.enemies_shot_group, sprite_groups.player_group, dokilla=False, dokillb=False, collided=None)

        if hits:
            for hit in hits:
                
                hit.kill()

