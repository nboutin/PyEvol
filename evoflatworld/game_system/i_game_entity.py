'''
Created on Aug 1, 2019

@author: nboutin
'''


class IGameEntity():

    def __init__(self, icontroller, iphysics, irender):
        self._icontroller = icontroller
        self._iphysics = iphysics
        self._irender = irender

        # why use a defered construction ?
#         if self._icontroller:
#             self._icontroller.build(self)
# 
#         if self._iphysics:
#             self._iphysics.build(self)
# 
#         if self._irender:
#             self._irender.build(self)

    @property
    def controller(self):
        return self._icontroller

    @property
    def physics(self):
        return self._iphysics

    @property
    def render(self):
        return self._irender
