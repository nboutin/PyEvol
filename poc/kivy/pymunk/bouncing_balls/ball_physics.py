'''
Created on 16 juil. 2019

@author: nboutin
'''

import pymunk


collision_types = {"creature": 1, "food": 2, }
categories = {"border": 0x01, "creature": 0x02, "food": 0x04, }


class BallPhysics():
    def __init__(self, **kwargs):
        """
        :param pos (x,y) (mandatory)
        :param radius (radians)
        :param angle, angle in radians
        :param space, Pymunk space (mandatory)

        Good value are radius:[10,50], mass:4, force:180
        """

        # Get parameters
        pos = kwargs['pos']
        radius = kwargs.get('radius')
        angle = kwargs.get('angle', 0)
        space = kwargs['space']
        force = kwargs.get('force', 180)
        mass = kwargs.get('mass', 4)

        # Pymunk
        self.__radius = radius
        self.__force = force

        moment = pymunk.moment_for_circle(mass, 0, self.__radius)

        self.__body = pymunk.Body(mass, moment)
        self.__body.position = pos
        self.__body.angle = angle

        self.__shape = pymunk.Circle(self.__body, self.__radius)
        self.__shape.elasticity = 0.95    # bounce realism
        self.__shape.friction = 0.9       # 0:frictionless

        self.__shape.collision_type = collision_types['creature']
        self.__shape.filter = pymunk.ShapeFilter(
            categories=categories['creature'])

        space.add(self.__body, self.__shape)

    @property
    def pos(self):
        return self.__body.position.int_tuple

    def move(self):
        powers = [10, 10]
        p1 = powers[0] * self.__force
        p2 = powers[1] * self.__force
        self.__body.apply_force_at_local_point((p1, 0), (0, -self.__radius))
        self.__body.apply_force_at_local_point((p2, 0), (0, +self.__radius))
        return self.pos
