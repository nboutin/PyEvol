'''
Created on Aug 1, 2019

@author: nboutin
'''
import pymunk as pm

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
        eye_radius = 3

        # Pymunk
        self._radius = radius

        moment = pm.moment_for_circle(mass, 0, self._radius)

        # Body
        self._body = pm.Body(mass, moment)
        self._body.position = pos      # circle center
        self._body.angle = angle

        # Body shape
        self._body_shape = pm.Circle(self._body, self._radius)
        self._body_shape.elasticity = 0.95    # bounce realism
        self._body_shape.friction = 0.9       # 0:frictionless

        self._body_shape.collision_type = collision_types['creature']
        self._body_shape.filter = pm.ShapeFilter(
            categories=categories['creature'])

        # Eye shape
        # Todo: create class
        qradius = radius / 2  # eye positon from body center
        self._eye_left_shape = pm.Circle(
            self._body, eye_radius, (qradius, qradius))
        self._eye_right_shape = pm.Circle(
            self._body, eye_radius, (qradius, -qradius))

        space.add(self._body, self._body_shape,
                  self._eye_left_shape, self._eye_right_shape)

    def update(self, game_entity, world, dt):
        """physics code..."""
        if game_entity._is_selected:
            # with manual control decrease power overtime untill zero
            game_entity.powers = [max(x - .3, 0) for x in game_entity.powers]

        p1, p2 = [x * self._power for x in game_entity.powers]

        self._body.apply_force_at_local_point((p1, 0), (0, -self._radius))
        self._body.apply_force_at_local_point((p2, 0), (0, +self._radius))

        game_entity.body_bb = self._body_shape.bb
        game_entity.eye_left_bb = self._eye_left_shape.bb
        game_entity.eye_right_bb = self._eye_right_shape.bb
