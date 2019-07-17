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


class GameSystem():

    def __init__(self):
        self._exit = False

        self._world = self._create_world()

        # TODO for better data locality use a list for each component type
        self._entities = list()

        #         Clock.schedule_interval(self.run, 1.0 / 60.0)

    @property
    def widget(self):
        return self._world.render

    def run(self):

        while not self._exit:
            for entity in self._entities:
                entity.controller.update(entity)

            for entity in self._entities:
                # second arg is world(physics)
                entity.physics.update(entity, None)

            for entity in self._entities:
                # second arg is render(graphics)
                entity.render.render(entity, None)

            # TODO add some game_loop timing

    def _create_world(self):
        return GameEntity(None, WorldPhysics(), WorldRender())

    def create_ball(self):
        # TODO add to entities list
        return GameEntity(KeyboardController(), BallPhysics(), BallRender())
