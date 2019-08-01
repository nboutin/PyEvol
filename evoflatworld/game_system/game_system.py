'''
Created on Aug 1, 2019

@author: nboutin
'''

from kivy.clock import Clock
from evoflatworld.game_system.world_entity import WorldEntity
from evoflatworld.game_system.world_render_strategy import WorldRenderStrategy
from evoflatworld.game_system.creature_entity import CreatureEntity
from evoflatworld.game_system.creature_render_strategy import CreatureRenderStrategy
from evoflatworld.game_system.world_physics_strategy import WorldPhysicsStrategy
from evoflatworld.game_system.creature_physics_strategy import CreaturePhysicsStrategy


class GameSystem():

    def __init__(self):
        '''
        TODO for better data locality use a list for each component type
        '''
        self._entities = list()

        self._world = self._create_world()

        self._create_creature()

        # call -1:before, 0:after the next frame
        Clock.schedule_interval(self._run, 0)

    def _run(self, dt):

        # Physics
        for entity in self._entities:
            if entity.physics:
                entity.physics.update(entity, None, dt)

        self._world.physics.update(None, None, dt)

        # Graphics
        for entity in self._entities:
            if entity.render:
                entity.render.render(entity, None)

    @property
    def widget(self):
        return self._world.render

    def _create_world(self):
        return WorldEntity(None, WorldPhysicsStrategy(), WorldRenderStrategy())

    def _create_creature(self):
        pos = self._world.render.center
        diameter = 10

        creature_entity = CreatureEntity(
            None,
            CreaturePhysicsStrategy(pos, diameter, self._world.physics.space),
            CreatureRenderStrategy(pos, diameter, self._world.render), pos, diameter)

        self._entities.append(creature_entity)
