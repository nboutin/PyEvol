import pygame


class Axis:
    def __init__(self, r):
        (self.x_min, self.x_max, self.y_min, self.y_max) = 0, 10 + 1, 0, 10 + 1
        (self.x_origin, self.y_origin) = r.left + r.w / 10, r.bottom - r.h / 10

        x_px_length = r.right - self.x_origin
        self.x_px_step = x_px_length / (self.x_max - self.x_min)

        y_px_length = self.y_origin - r.top
        self.y_px_step = y_px_length / (self.y_max - self.y_min)

    def axis(self, val):
        (self.x_min, self.x_max, self.y_min, self.y_max) = val
        self.x_max += 1
        self.y_max += 1

    def x_to_pygame(self, x):
        return self.x_origin + x * self.x_px_step

    def y_to_pygame(self, y):
        return self.y_origin - y * self.y_px_step

class Graph:
    ANTIALIAS = 1
    COLOR_FONT = pygame.color.THECOLORS['black']

    def __init__(self, size):
        self.r = pygame.rect.Rect((0, 0), size)

        self.axis = Axis(self.r)

        self.font = pygame.font.SysFont("monospace", 15)

    def plot(self, data):

        # create surface
        s = pygame.surface.Surface(self.r.size)

        # background is white
        s.fill(pygame.color.THECOLORS['white'])

        self.axis.x_max = max(self.axis.x_max, len(data))
        self.axis.y_max = max(self.axis.y_max, max(data))
        self.__draw_axis(s)

        if len(data) > 1:
            # draw data
            data_pointlist = [self.axis.y_to_pygame(y) for y in data]
            x_pointlist = [self.axis.x_to_pygame(x) for x in range(self.axis.x_max - self.axis.x_min)]

            pointlist = [(x, y) for (x, y) in zip(x_pointlist, data_pointlist)]

            pygame.draw.lines(s, pygame.color.THECOLORS['blue'], False, pointlist, 2)

        return s

    def __draw_axis(self, s):
        # X-axis
        pygame.draw.line(s, pygame.color.THECOLORS['black'],
                         (self.r.left, self.axis.y_origin),
                         (self.r.right, self.axis.y_origin),
                         2)

        # Y-axis
        pygame.draw.line(s, pygame.color.THECOLORS['black'],
                         (self.axis.x_origin, self.r.bottom),
                         (self.axis.x_origin, self.r.top),
                         2)

        # X scale
        for i in range(1, self.axis.x_max - self.axis.x_min):
            pygame.draw.line(s, pygame.color.THECOLORS['red'],
                             (self.axis.x_to_pygame(i), self.axis.y_origin - 5),
                             (self.axis.x_to_pygame(i), self.axis.y_origin + 5),
                             2)

            text = '{}'.format(i)
            s.blit(self.__blit(text), (self.axis.x_to_pygame(i), self.axis.y_origin + 5))

        # Y scale
        for i in range(1, int(self.axis.y_max - self.axis.y_min), 5):
            pygame.draw.line(s, pygame.color.THECOLORS['red'],
                             (self.axis.x_origin - 5, self.axis.y_to_pygame(i)),
                             (self.axis.x_origin + 5, self.axis.y_to_pygame(i)),
                             2)

            text = '{}'.format(i)
            (w, h) = self.font.size(text)
            s.blit(self.__blit(text), (self.axis.x_origin - 5 - w, self.axis.y_to_pygame(i)))

        return s

    def __blit(self, text):
        return self.font.render(text, Graph.ANTIALIAS, Graph.COLOR_FONT)
