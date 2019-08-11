'''
Created on Aug 11, 2019

@author: nboutin
'''
from kivy.graphics import Ellipse


def make_ellipse_from_circle(shape):
    '''
    :param shape: pymunk.Shape
    :return kivy.graphics.Ellipse
    '''
    radius = shape.radius
    diameter = radius * 2
    pos = shape.body.position - (radius, radius)
    return Ellipse(pos=pos, size=[diameter, diameter])


def update_ellipse_from_circle(ellipse, shape):
    '''
    :param ellipse: kivy.graphics.Ellipse
    :param shape: pymunk.Shape
    '''
    body = shape.body
    radius = shape.radius
    ellipse.pos = body.position - (radius, radius)
    # todo: update size
