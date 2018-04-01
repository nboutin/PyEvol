import cocos
from cocos.director import director
from cocos.scenes import FadeTRTransition

from pyglet import clock

from main_menu import MainMenu

PARAM = {
    'window':{
            'fullscreen': True,
            'resizable': True,
            'vsync' : True,
            'caption': 'PyEvol',
            'autoscale': True,
        }
    }

class Intro(cocos.layer.Layer):
    
    def __init__(self):
        super(Intro, self).__init__()
        
        w, h = director.get_window_size()
        self.text = cocos.text.Label("PyEvol",
                                     font_size = 48,
                                     anchor_x = 'center',
                                     anchor_y = 'center',
                                     position = (w/2, h/2))
        self.add(self.text)
        
        clock.schedule_once(self.clock_cb, 2)
        
    def clock_cb(self, dt):
        director.replace(cocos.scene.Scene(MainMenu()))


if __name__ == '__main__':
    
    director.init(**PARAM['window'])
    director.show_FPS = True;
    director.run(cocos.scene.Scene(Intro()))

