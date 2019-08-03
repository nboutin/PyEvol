'''
Created on Aug 1, 2019

@author: nboutin
'''

from kivy.clock import Clock
from evoflatworld.game_system.world_entity import WorldEntity
from evoflatworld.game_system.world_render_scatter_strategy import WorldRenderScatterStrategy
from evoflatworld.game_system.world_render_widget_strategy import WorldRenderWidgetStrategy
from evoflatworld.game_system.creature_entity import CreatureEntity
from evoflatworld.game_system.creature_render_strategy import CreatureRenderStrategy
from evoflatworld.game_system.world_physics_strategy import WorldPhysicsStrategy
from evoflatworld.game_system.creature_physics_strategy import CreaturePhysicsStrategy

import math
import random


class GameSystem():

    def __init__(self):
        '''
        TODO for better data locality use a list for each component type
        '''
        self._entities = list()

        self._world = self._create_world()

        for _ in range(0, 1):
            self._create_creature()

        # call -1:before, 0:after the next frame
        Clock.schedule_interval(self._run, 0)

    def _run(self, dt):

        # Physics
        for entity in self._entities:
            if entity.physics:
                entity.physics.update(entity, None, dt)

        self._world.physics.update(self._world, None, dt)

        # Graphics
        for entity in self._entities:
            if entity.render:
                entity.render.render(entity, self._world.render)

        self._world.render.render(self._world, None)

    @property
    def widget(self):
        return self._world.render

    def _create_world(self):
        pos = (0, 0)
        size = (500, 500)

        return WorldEntity(
            None,
            WorldPhysicsStrategy(),
            # WorldRenderScatterStrategy(size=size, pos=pos,
            WorldRenderWidgetStrategy(size=size, pos=pos),
            pos, size)

    def _create_creature(self):
        #         pos = self._world.render.center
        pos = (100, 100)
        diameter = 10
        angle = math.radians(random.randint(-180, 180))

        creature_entity = CreatureEntity(
            None,
            CreaturePhysicsStrategy(
                pos, diameter, angle, self._world.physics.space),
            CreatureRenderStrategy(pos, diameter, self._world.render), pos, diameter)

        self._entities.append(creature_entity)
