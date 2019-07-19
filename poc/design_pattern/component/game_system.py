'''
Created on 17 juil. 2019

@author: f24178c
'''

from kivy.clock import Clock

from component.game_entity import GameEntity
from entity.world_render import WorldRender
from entity.world_physics import WorldPhysics
from entity.keyboard_controller import KeyboardController
from entity.ball_physics import BallPhysics
from entity.ball_render import BallRender

from random import (random, uniform, randint)


class GameSystem():

    def __init__(self):
        # TODO for better data locality use a list for each component type
        self._entities = list()

        self._world = self._create_world()

        Clock.schedule_interval(self.run, 0)

    @property
    def widget(self):
        return self._world.render

    def run(self, dt):

        for entity in self._entities:
            if entity.controller:
                entity.controller.update(entity)

        for entity in self._entities:
            # second arg is world(physics)
            if entity.physics:
                entity.physics.update(entity, None)
        
        self._world.space.step(dt)

        for entity in self._entities:
            # second arg is render(graphics)
            if entity.render:
                entity.render.render(entity, None)

        # TODO add some game_loop timing

    def _create_world(self):
        return GameEntity(None, WorldPhysics(), WorldRender(self))

    def _create_ball(self, pos):
        # entity = GameEntity(KeyboardController(), BallPhysics(), BallRender())
#         pos = (random() * self.widget.width + self.widget.x,
#                random() * self.widget.height + self.widget.y)

        entity = GameEntity(None, None, BallRender(
            pos=pos, widget=self.widget))
        self._entities.append(entity)
        return entity
