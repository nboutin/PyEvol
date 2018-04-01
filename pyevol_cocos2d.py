import cocos
from cocos.director import director

# import pyglet

PARAM = {
    'window':{
            'fullscreen': True,
            'resizable': True,
            'vsync' : True,
            'caption': 'PyEvol',
            'autoscale': True
        }
    }

class Intro(cocos.layer.Layer):
    def __init__(self):
        super(Intro, self).__init__()
        
        h, w = director.get_window_size()
        self.text = cocos.text.Label("PyEvol",
                                     font_size = 48,
                                     anchor_x = 'center',
                                     anchor_y = 'center',
                                     position = (h/2, w/2))
        self.add(self.text)

if __name__ == '__main__':
    director.init(**PARAM['window'])
    
    director.run(cocos.scene.Scene(Intro()))
