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
        handler.begin = creature_eat_food

    @property
    def space(self):
        return self._space

def creature_eat_food(arbiter, space, data):
    creature = arbiter.shapes[0].controller
    food = arbiter.shapes[1].controller
    
    if creature and food:
        creature.eat(food)
        
    return True
