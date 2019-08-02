'''
Created on Aug 1, 2019

@author: nboutin
'''
import pymunk

from evoflatworld.game_system.i_physics_strategy import IPhysicsStrategy


class WorldPhysicsStrategy(IPhysicsStrategy):

    def __init__(self):
        '''
        Todo: construct space outside world_physics_strategy and pass it by update
              game_system should have the space instance  
        '''
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)
        self._space.damping = 0.1  # lose 1-x% of its velocity per second

    @property
    def space(self):
        return self._space

    def update(self, game_entity, world, dt):

        # Handle donut world for each body in space
        for body in self._space.bodies:

            bx = body.position.x
            by = body.position.y
            shape = next(iter(body.shapes))
            bb = shape.bb
            radius = shape.radius

#             print ("game_entity.size:", game_entity.size)

            world_right = game_entity.size[0]
            world_left = 0
            world_down = 0
            world_up = game_entity.size[1]

            if bb.right > world_right:
                body.position = (world_left + radius, by)
                self._space.reindex_shapes_for_body(body)
            elif bb.left < world_left:
                body.position = (world_right - radius, by)
                self._space.reindex_shapes_for_body(body)
            elif bb.top > world_up:
                body.position = (bx, world_down + radius)
                self._space.reindex_shapes_for_body(body)
            elif bb.bottom < world_down:
                body.position = (bx, world_up - radius)
                self._space.reindex_shapes_for_body(body)

        self._space.step(dt)
