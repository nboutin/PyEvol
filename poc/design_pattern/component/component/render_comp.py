'''
Created on 17 juil. 2019

@author: nboutin
'''


class RenderComp():

    def build(self, game_entity, **kwargs):
        raise NotImplementedError()

    def render(self, game_entity, render):
        raise NotImplementedError()
