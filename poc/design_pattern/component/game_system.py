'''
Created on 17 juil. 2019

@author: f24178c
'''

from component.game_entity import GameEntity

from entity.world_render import WorldRender
from entity.general_input import GeneralInput
from entity.ball_physics import BallPhysics
from entity.ball_render import BallRender


class GameSystem():

    def __init__(self):
        self._exit = False

        # TODO for better data locality use a list for each component type
        self._entities = list()

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
        # TODO add to entities list
        return GameEntity(None, None, WorldRender())

    def create_ball(self):
        # TODO add to entities list
        return GameEntity(GeneralInput(), BallPhysics(), BallRender())
