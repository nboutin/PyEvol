'''
Created on Aug 11, 2019

@author: nboutin
'''
import pymunk as pm

from evoflatworld.game_system.i_physics_strategy import IPhysicsStrategy
from evoflatworld.game_system.physics_controller import (
    collision_types, categories)


class FoodPhysicsStrategy(IPhysicsStrategy):

    def __init__(self, pos, radius, space):

        # Parameters
        __MASS = 200

        # Pymunk
        moment = pm.moment_for_circle(__MASS, 0, radius)

        # Body
        self._body = pm.Body(__MASS, moment)
        self._body.position = pos
        self._body.angle = 0

        # Shape
        self._body_shape = pm.Circle(self._body, radius)
#         self._body_shape.sensor = True
        self._body_shape.collision_type = collision_types['food']
        self._body_shape.filter = pm.ShapeFilter(categories=categories['food'])

        # Space
        space.add(self._body, self._body_shape)

    def update(self, game_entity, world, dt):
        game_entity.body_shape = self._body_shape
