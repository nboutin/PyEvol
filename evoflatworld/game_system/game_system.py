'''
Created on Aug 1, 2019

@author: nboutin
'''
import math
import random

from kivy.clock import Clock
from kivy.utils import get_random_color

from evoflatworld.game_system.world_entity import WorldEntity
from evoflatworld.game_system.world_render_scatter_strategy import WorldRenderScatterStrategy
from evoflatworld.game_system.world_render_widget_strategy import WorldRenderWidgetStrategy
from evoflatworld.game_system.creature_entity import CreatureEntity
from evoflatworld.game_system.creature_render_strategy import CreatureRenderStrategy
from evoflatworld.game_system.creature_controller_strategy import CreatureControllerStrategy
from evoflatworld.game_system.world_physics_strategy import WorldPhysicsStrategy
from evoflatworld.game_system.creature_physics_strategy import CreaturePhysicsStrategy
import colors


class GameSystem():

    def __init__(self):
        '''
        TODO for better data locality use a list for each component type
        '''
        self._entities = list()

        self._world = self._create_world()

        for _ in range(0, 1):
            self._create_creature()

        self._is_play = True
        self._step = 0.0
        self._physics_step = 1.0 / 30  # time step
        self._lag = 0.0
        self._physics_multiplier = .25

        # call -1:before, 0:after the next frame
        self._trigger = Clock.create_trigger(self._run)
        self._trigger()

    @property
    def widget(self):
        return self._world.render

    def play(self):
        self._is_play = True

    def pause(self):
        self._is_play = False

    def step(self):
        '''Use mutex to synchronize with run method ?'''
        self.pause()
        self._step = self._physics_step

    def speed_down(self):
        self._physics_multiplier /= 2

    def speed_up(self):
        self._physics_multiplier *= 2

    @property
    def speed(self):
        return self._physics_multiplier

    def _run(self, dt):

        # Controller
        for entity in self._entities:
            if entity.controller:
                entity.controller.update(entity)

        # Physics
        if self._is_play or self._step > 0:

            dt *= self._physics_multiplier

            self._lag += self._step if (self._step > 0) else dt
            self._step = 0

            while self._lag >= self._physics_step:

                self._lag -= self._physics_step

                for entity in self._entities:
                    if entity.physics:
                        entity.physics.update(
                            entity, None, self._physics_step)

                self._world.physics.update(
                    self._world, None, self._physics_step)

        # Graphics
        for entity in self._entities:
            if entity.render:
                entity.render.render(entity, self._world.render)

        self._world.render.render(self._world, None)

        self._trigger()

    def _create_world(self):
        pos = (50, 50)
        size = (1200, 700)

        return WorldEntity(
            None,
            WorldPhysicsStrategy(),
            # WorldRenderScatterStrategy(size=size, pos=pos,
            WorldRenderWidgetStrategy(size=size, pos=pos),
            pos, size)

    def _create_creature(self):
        pos = (random.randint(0, 1200), random.randint(0, 700))
        diameter = 30
        angle = math.radians(random.randint(-180, 180))
#         color = get_random_color()
        color = colors.Gray

        creature_entity = CreatureEntity(
            CreatureControllerStrategy(),
            CreaturePhysicsStrategy(
                pos, diameter, angle, self._world.physics.space),
            CreatureRenderStrategy(pos, diameter, color, self._world.render), pos, diameter)

        self._entities.append(creature_entity)
