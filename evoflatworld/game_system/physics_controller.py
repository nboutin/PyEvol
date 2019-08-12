'''
Created on Aug 11, 2019

@author: nboutin
'''
import pymunk

collision_types = {'creature': 1, 'food': 2, }
categories = {'border': 0x01, 'creature': 0x02, 'food': 0x04, }


class PhysicsController():

    def __init__(self):

        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)
        self._space.damping = 0.1  # lose 1-x% of its velocity per second

        handler = self._space.add_collision_handler(
            collision_types['creature'],
            collision_types['food'])
#         handler.post_solve = post_solve_food
        handler.begin = begin_food

    @property
    def space(self):
        return self._space


def post_solve_food(arbiter, space, data):
    #     print(arbiter, space, data)
    print(arbiter.contact_point_set, arbiter.is_first_contact)
    for s in arbiter.shapes:
        print(s.bb)


def begin_food(arbiter, space, data):
    print("begin")
    print(arbiter.contact_point_set, arbiter.is_first_contact)
    for s in arbiter.shapes:
        print(s.bb)
