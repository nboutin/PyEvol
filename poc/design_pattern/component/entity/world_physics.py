'''
Created on Jul 17, 2019

@author: nboutin
'''

from component.physics_comp import PhysicsComp
import pymunk


class WorldPhysics(PhysicsComp):

    def __init__(self):
        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)
        self._space.damping = 0.1  # lose 1-x% of its velocity per second

    def build(self, game_entity, **kwargs):
        pass

    @property
    def space(self):
        return self._space

    def update(self, game_entity, world, dt):
        self._space.step(dt)