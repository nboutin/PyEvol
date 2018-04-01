import cocos.menu
from cocos.menu import *

import pyglet

class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__('PyEvol')
        
        self.menu_anchor_x = CENTER
        self.menu_anchor_y = CENTER
        
        items = []
        items.append(MenuItem('Start simulation', self.on_start))
        items.append(MenuItem('Options', self.on_options))
        items.append(MenuItem('Quit', self.on_quit))
        
        self.create_menu(items, shake(), shake_back())
        
    def on_start(self):
        pass
    
    def on_options(self):
        pass
    
    def on_quit(self):
        pyglet.app.exit()
        
        