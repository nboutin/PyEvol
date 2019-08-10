'''
Created on 17 juil. 2019

@author: nboutin
'''


class ControllerComp():

    def build(self, game_entity):
        raise NotImplementedError()

    def update(self, game_entity):
        raise NotImplementedError()
