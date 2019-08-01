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

    def __init__(self, pos, diameter, space):
        '''
        Good value are radius:[10,50], mass:4, force:180
        '''

        # Parameters
        radius = diameter / 2
        angle = 0
        force = 180
        mass = 4

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

    def update(self, game_entity, world, dt):
        """physics code..."""
        powers = [2, 2]
        p1 = powers[0] * self.__force
        p2 = powers[1] * self.__force
        self.__body.apply_force_at_local_point((p1, 0), (0, -self.__radius))
        self.__body.apply_force_at_local_point((p2, 0), (0, +self.__radius))

        game_entity.pos = self.__body.position.int_tuple
