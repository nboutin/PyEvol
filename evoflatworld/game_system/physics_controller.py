'''
Created on Aug 11, 2019

@author: nboutin
'''
import pymunk

collision_types = {'border': 1, 'creature': 2, 'food': 3, }
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

        handler = self._space.add_collision_handler(
            collision_types['border'],
            collision_types['creature'])
        handler.begin = border_out

    @property
    def space(self):
        return self._space


def creature_eat_food(arbiter, space, data):
    creature = arbiter.shapes[0].controller
    food = arbiter.shapes[1].controller

    if creature and food:
        creature.eat(food)

    return True


# left
# BB(-20.0, -10.0, 0.0, 410.0)
# <pymunk.shapes.Circle object at 0x7fe3ccd56550>
def border_out(arbiter, space, data):
    border, creature = arbiter.shapes

    print(border.side)
    print(border.bb)
    print(creature)

    x, y = creature.body.position

    if border.side == 'left':
        pass
    elif border.side == 'top':
        creature.body.position = (x, 0 + creature.radius)
    elif border.side == 'right':
        creature.body.position = (0 + creature.radius, y)
    elif border.side == 'bottom':
        pass

    return True
