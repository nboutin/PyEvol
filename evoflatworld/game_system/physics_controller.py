'''
Created on Aug 11, 2019

@author: nboutin
'''
import pymunk

collision_types = {'border': 1, 'creature': 2, 'food': 3, }
categories = {'border': 0x01, 'creature': 0x02, 'food': 0x04, }


class PhysicsController():

    def __init__(self, world_size, game_system):

        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)
        self._space.damping = 0.1  # lose 1-x% of its velocity per second

        # Creature and Food
        self._space.on_collision(
            collision_types['creature'],
            collision_types['food'],
            begin=creature_eat_food,
            data={'game_system': game_system}
        )

        # Border and Creature
        self._space.on_collision(
            collision_types['border'],
            collision_types['creature'],
            begin=border_out,
            data={'world_size': world_size}
        )

    @property
    def space(self):
        return self._space


def creature_eat_food(arbiter, space, data):
    creature = arbiter.shapes[0].game_entity
    food = arbiter.shapes[1].game_entity
    game_system = data['game_system']
    
    try:
        creature().physics.eat(food().physics)

        # If food has no more calories, remove it from game_system
        if not food().calories > 0:
            game_system.remove_food(food())
    except AttributeError:
        pass

    return True


def border_out(arbiter, space, data):
    border, creature = arbiter.shapes

    x, y = creature.body.position
    ww, wh = data['world_size']

    if border.side == 'left':
        creature.body.position = (ww - creature.radius, y)
    elif border.side == 'top':
        creature.body.position = (x, 0 + creature.radius)
    elif border.side == 'right':
        creature.body.position = (0 + creature.radius, y)
    elif border.side == 'bottom':
        creature.body.position = (x, wh - creature.radius)

    return True
