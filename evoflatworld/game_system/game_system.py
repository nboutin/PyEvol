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
from kivy.utils import get_random_color

import math
import random


class GameSystem():

    def __init__(self):
        '''
        TODO for better data locality use a list for each component type
        '''
        self._entities = list()

        self._world = self._create_world()

        for _ in range(0, 3):
            self._create_creature()

        self.__is_play = True
        self.__step = 0.0
        self.__physics_step = 1.0 / 30  # time step
        self.__lag = 0.0
        self.__physics_iteration = 2

        # call -1:before, 0:after the next frame
        self.__trigger = Clock.create_trigger(self._run)
        self.__trigger()

    @property
    def widget(self):
        return self._world.render

    def play(self):
        self.__is_play = True

    def pause(self):
        self.__is_play = False

    def step(self):
        '''Use mutex to synchronize with run method ?'''
        self.pause()
        self.__step = self.__physics_step

    def speed_down(self):
        self.__physics_iteration /= 2

    def speed_up(self):
        self.__physics_iteration *= 2

    def _run(self, dt):

        if self.__is_play or self.__step > 0:
            self.__lag += self.__step if (self.__step > 0) else dt
            self.__step = 0

            # Physics
            while self.__lag >= self.__physics_step:

                self.__lag -= self.__physics_step

                for _ in range(0, int(self.__physics_iteration)):

                    for entity in self._entities:
                        if entity.physics:
                            entity.physics.update(
                                entity, None, self.__physics_step)

                    self._world.physics.update(
                        self._world, None, self.__physics_step)

        # Graphics
        for entity in self._entities:
            if entity.render:
                entity.render.render(entity, self._world.render)

        self._world.render.render(self._world, None)

        self.__trigger()

    def _create_world(self):
        pos = (0, 0)
        size = (600, 550)

        return WorldEntity(
            None,
            WorldPhysicsStrategy(),
            # WorldRenderScatterStrategy(size=size, pos=pos,
            WorldRenderWidgetStrategy(size=size, pos=pos),
            pos, size)

    def _create_creature(self):
        #         pos = self._world.render.center
        pos = (100, 100)
        diameter = 30
        angle = math.radians(random.randint(-180, 180))
        color = get_random_color()

        creature_entity = CreatureEntity(
            None,
            CreaturePhysicsStrategy(
                pos, diameter, angle, self._world.physics.space),
            CreatureRenderStrategy(pos, diameter, color, self._world.render), pos, diameter)

        self._entities.append(creature_entity)
