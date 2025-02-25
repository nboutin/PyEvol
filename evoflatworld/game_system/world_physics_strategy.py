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

        # World
        wx, wy = game_entity.pos
        ww, wh = game_entity.size
        world_bb = pymunk.BB(wx, wy, ww + wx, wh + wy)

        # Handle donut world for each body in space
        for body in self._space.bodies:

            # Body
            bx, by = body.position
            shape = next(iter(body.shapes))
            bb = shape.bb
            radius = shape.radius

            if bb.right > world_bb.right:
                body.position = (world_bb.left + radius, by)
                self._space.reindex_shapes_for_body(body)
            elif bb.left < world_bb.left:
                body.position = (world_bb.right - radius, by)
                self._space.reindex_shapes_for_body(body)
            elif bb.top > world_bb.top:
                body.position = (bx, world_bb.bottom + radius)
                self._space.reindex_shapes_for_body(body)
            elif bb.bottom < world_bb.bottom:
                body.position = (bx, world_bb.top - radius)
                self._space.reindex_shapes_for_body(body)

        self._space.step(dt)
