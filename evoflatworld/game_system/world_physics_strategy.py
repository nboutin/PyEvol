'''
Created on Aug 1, 2019

@author: nboutin
'''
import pymunk

from evoflatworld.game_system.i_physics_strategy import IPhysicsStrategy


class WorldPhysicsStrategy(IPhysicsStrategy):

    def __init__(self):
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)
        self._space.damping = 0.1  # lose 1-x% of its velocity per second

    @property
    def space(self):
        return self._space

    def update(self, game_entity, world, dt):

        for body in self._space.bodies:
            
            bx = body.position.x
            by = body.position.y
            
            world_right = 0
            world_left = game_entity.size[0]
            world_down = 0
            world_up = game_entity.size[1]
            
            # print shape
            
            if bx > world_left:
                body.position = (world_right, by)
                self._space.reindex_shapes_for_body(body)
            elif bx < world_right:
                body.position = (world_left, by)
                self._space.reindex_shapes_for_body(body)
            elif by > world_up:
                body.position = (bx, world_down)
                self._space.reindex_shapes_for_body(body)
            elif by < world_down:
                body.position = (bx, world_up)
                self._space.reindex_shapes_for_body(body)
                
        self._space.step(dt)
