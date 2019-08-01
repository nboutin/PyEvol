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
            if body.position.x > game_entity.size[0]:
                body.position = (0, body.position.y)
                self._space.reindex_shapes_for_body(body)

        self._space.step(dt)
