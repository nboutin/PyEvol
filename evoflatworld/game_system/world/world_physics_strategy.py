'''
Created on Aug 1, 2019

@author: nboutin
'''
import pymunk

from evoflatworld.game_system.i_physics_strategy import IPhysicsStrategy


class WorldPhysicsStrategy(IPhysicsStrategy):

    def __init__(self):
        pass
    
    def update(self, game_entity, world, dt):

        # World
        ww, wh = game_entity.size
        world_bb = pymunk.BB(0, 0, ww, wh)

        # Handle donut world for each body in space
        for body in world.bodies:

            # Body
            bx, by = body.position
            shape = next(iter(body.shapes))
            bb = shape.bb
            radius = shape.radius

            if bb.right > world_bb.right:
                body.position = (world_bb.left + radius, by)
                world.reindex_shapes_for_body(body)
            elif bb.left < world_bb.left:
                body.position = (world_bb.right - radius, by)
                world.reindex_shapes_for_body(body)
            elif bb.top > world_bb.top:
                body.position = (bx, world_bb.bottom + radius)
                world.reindex_shapes_for_body(body)
            elif bb.bottom < world_bb.bottom:
                body.position = (bx, world_bb.top - radius)
                world.reindex_shapes_for_body(body)
