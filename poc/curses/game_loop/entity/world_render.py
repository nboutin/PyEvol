'''
Created on 17 juil. 2019

@author: nboutin
'''

from component.render_comp import RenderComp
from utils import Rectangle
import curses


class WorldRender(RenderComp):

    def __init__(self):
        super().__init__()
        
        r = Rectangle(0,0,200,200)
        self._window = curses.newwin(r.h, r.w, r.y, r.x)
        
    def render(self, game_entity, render):
        """graphics code ..."""
        self._window.refresh()
