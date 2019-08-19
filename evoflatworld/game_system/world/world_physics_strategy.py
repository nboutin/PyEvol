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
        self._body = pm.Body(0, 0, pm.Body.STATIC)

        # Shapes
        __THICKNESS = 10
        self._left = pm.Segment(self._body, (0, 0), (0, h), __THICKNESS)
        self._top = pm.Segment(self._body, (0, h), (w, h), __THICKNESS)

        for s in [self._left, self._top]:
            s.sensor = True
            s.collision_type = collision_types['border']
            s.filter = pm.ShapeFilter(categories=categories['border'])

        # Space
        space.add(self._body, self._left, self._top)

    def update(self, game_entity, world, dt):
        pass

#         # World
#         ww, wh = game_entity.size
#         world_bb = pm.BB(0, 0, ww, wh)
#
#         # Handle donut world for each body in space
#         for body in world.bodies:
#
#             # Body
#             bx, by = body.position
#             shape = next(iter(body.shapes))
#             bb = shape.bb
#             radius = shape.radius
#
#             if bb.right > world_bb.right:
#                 body.position = (world_bb.left + radius, by)
#                 world.reindex_shapes_for_body(body)
#             elif bb.left < world_bb.left:
#                 body.position = (world_bb.right - radius, by)
#                 world.reindex_shapes_for_body(body)
#             elif bb.top > world_bb.top:
#                 body.position = (bx, world_bb.bottom + radius)
#                 world.reindex_shapes_for_body(body)
#             elif bb.bottom < world_bb.bottom:
#                 body.position = (bx, world_bb.top - radius)
#                 world.reindex_shapes_for_body(body)
