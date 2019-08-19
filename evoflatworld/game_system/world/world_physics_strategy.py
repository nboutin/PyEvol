'''
Created on Aug 1, 2019

@author: nboutin
'''
import pymunk as pm

from evoflatworld.game_system.physics_controller import (
    categories, collision_types)
from evoflatworld.game_system.i_physics_strategy import IPhysicsStrategy


class WorldPhysicsStrategy(IPhysicsStrategy):

    def __init__(self, size, space):

        # Parameters
        w, h = size

        # Pymunk

        # Body
        body = pm.Body(0, 0, pm.Body.STATIC)

        # Shapes
        __THICKNESS = 10
        x = 0 - __THICKNESS
        left = pm.Segment(body, (x, 0), (x, h), __THICKNESS)

        y = h + __THICKNESS
        top = pm.Segment(body, (0, y), (w, y), __THICKNESS)

        x = w + __THICKNESS
        right = pm.Segment(body, (x, h), (x, 0), __THICKNESS)

        y = 0 - __THICKNESS
        bottom = pm.Segment(body, (w, y), (0, y), __THICKNESS)

        for s, side in zip([left, top, right, bottom], ['left', 'top', 'right', 'bottom']):
            s.side = side
            s.sensor = True
            s.collision_type = collision_types['border']
            s.filter = pm.ShapeFilter(categories=categories['border'])

        # Space
        space.add(body, left, top, right, bottom)

    def update(self, game_entity, world, dt):
        pass
