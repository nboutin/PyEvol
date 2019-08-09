'''
Created on Aug 1, 2019

@author: nboutin
'''
import pymunk

from evoflatworld.game_system.i_physics_strategy import IPhysicsStrategy

# Todo: find a better place for this
collision_types = {"creature": 1, "food": 2, }
categories = {"border": 0x01, "creature": 0x02, "food": 0x04, }


class CreaturePhysicsStrategy(IPhysicsStrategy):

    def __init__(self, pos, diameter, angle, space):
        '''
        Good value are radius:[10,50], mass:4, power:180
        :param angle in radians
        '''

        # Parameters
        self._power = 180
        mass = 4
        radius = diameter / 2
        angle = angle

        # Pymunk
        self._radius = radius

        moment = pymunk.moment_for_circle(mass, 0, self._radius)

        self._body = pymunk.Body(mass, moment)
        self._body.position = pos      # circle center
        self._body.angle = angle

        self._shape = pymunk.Circle(self._body, self._radius)
        self._shape.elasticity = 0.95    # bounce realism
        self._shape.friction = 0.9       # 0:frictionless

        self._shape.collision_type = collision_types['creature']
        self._shape.filter = pymunk.ShapeFilter(
            categories=categories['creature'])

        space.add(self._body, self._shape)

    def update(self, game_entity, world, dt):
        """physics code..."""
        if game_entity._is_selected:
            game_entity.powers = [max(x - .1, 0) for x in game_entity.powers]

        p1, p2 = [x * self._power for x in game_entity.powers]

        self._body.apply_force_at_local_point((p1, 0), (0, -self._radius))
        self._body.apply_force_at_local_point((p2, 0), (0, +self._radius))

        game_entity.pos = self._body.position.int_tuple
