'''
Created on Aug 1, 2019

@author: nboutin
'''
import math
import random

from kivy.clock import Clock
from kivy.utils import get_random_color

from evoflatworld.utils.colors import Colors
import evoflatworld.parameters as param
from evoflatworld.game_system.world.world_entity import WorldEntity
from evoflatworld.game_system.world.world_physics_strategy import WorldPhysicsStrategy
from evoflatworld.game_system.world.world_render_scatter_strategy import WorldRenderScatterStrategy
from evoflatworld.game_system.world.world_render_widget_strategy import WorldRenderWidgetStrategy
from evoflatworld.game_system.creature.creature_entity import CreatureEntity
from evoflatworld.game_system.creature.creature_controller_strategy import CreatureControllerStrategy
from evoflatworld.game_system.creature.creature_physics_strategy import CreaturePhysicsStrategy
from evoflatworld.game_system.creature.creature_render_strategy import CreatureRenderStrategy
from evoflatworld.game_system.food.food_entity import FoodEntity
from evoflatworld.game_system.food.food_render_strategy import FoodRenderStrategy
from evoflatworld.game_system.food.food_physics_strategy import FoodPhysicsStrategy
from evoflatworld.game_system.physics_controller import PhysicsController


class GameSystem():

    def __init__(self):
        '''
        TODO for better data locality use a list for each component type
        '''
        self._physics_controller = PhysicsController(param.WORLD_SIZE, self)

        self._entities = list()

        self._world = self._create_world()

        for _ in range(0, param.FOOD_COUNT):
            self._create_food()

        for _ in range(0, param.CREATURE_COUNT):
            self._create_creature()

        self._is_play = True
        self._step = 0.0
        self._physics_step = 1.0 / 30  # time step
        self._physics_multiplier = 1.0
        self._lag = 0.0
        self._simulation_time = 0

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

    def remove_entity(self, entity):
        entity.render.remove()
        self._entities.remove(entity)

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

                self._simulation_time += self._physics_step
                self._lag -= self._physics_step

                for entity in self._entities:
                    if entity.physics:
                        entity.physics.update(
                            entity, None, self._physics_step)

                self._world.physics.update(
                    self._world, self._physics_controller.space, self._physics_step)

                self._physics_controller.space.step(self._physics_step)

        # Graphics
        for entity in self._entities:
            if entity.render:
                entity.render.render(entity, self._world.render)

        self._world.render.render(self._world, None)

        self._trigger()

    def _create_world(self):
        size = param.WORLD_SIZE

        return WorldEntity(
            None,
            WorldPhysicsStrategy(size, self._physics_controller.space),
            # WorldRenderScatterStrategy(size=size, pos=pos,
            WorldRenderWidgetStrategy(
                size=size, pos=(50, 50), size_hint=(None, None)), size)

    def _create_creature(self):
        w, h = param.WORLD_SIZE
        pos = (random.randint(0, w), random.randint(0, h))
        radius = 15
        angle = math.radians(random.randint(-180, 180))
#         angle = math.radians(180)
        color = get_random_color()
#         color = Colors.Gray

        creature_entity = CreatureEntity(
            CreatureControllerStrategy(),
            CreaturePhysicsStrategy(
                pos, radius, angle, self._physics_controller.space),
            CreatureRenderStrategy(pos, radius, color,
                                   self._world.render, size_hint=(None, None)))

        self._entities.append(creature_entity)

    def _create_food(self):

        w, h = param.WORLD_SIZE
        pos = (random.randint(0, w), random.randint(0, h))
        radius = 10

        food_entity = FoodEntity(
            None,
            FoodPhysicsStrategy(pos, radius, self._physics_controller.space),
            FoodRenderStrategy(
                pos, radius, self._world.render, size_hint=(None, None)))

        self._entities.append(food_entity)
