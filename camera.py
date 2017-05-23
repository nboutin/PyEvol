import pygame


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Camera:

    ZOOM_STEP = 40
    MOVE_STEP = 100

    def __init__(self, world, area):
        # self.screen = screen
        # self.pos = pygame.rect.Rect(area)  # Position on screen
        # self.pos.center = screen.center

        self.world = world
        self.area = area  # Area of world
        self.area.center = self.world.center
        self.r_zoom = pygame.rect.Rect(world)

        self.surf_trans = None
        # self.is_transform_updated = True

    def get_surface(self, world):
        # if self.is_transform_updated:
        #     self.is_transform_updated = False
        #     self.surf_trans = pygame.transform.scale(world, self.r_zoom.size)
        # return self.surf_trans
        return pygame.transform.scale(world, self.r_zoom.size)

    def process_input(self, events):

        is_zoom_updated = False
        is_move_updated = False

        move = Point(0, 0)
        zoom = 0

        for event in events:

            # Keyboard
            if event.type == pygame.KEYDOWN:
                is_move_updated = True

                if event.key == pygame.K_q:
                    move.x += -Camera.MOVE_STEP
                elif event.key == pygame.K_d:
                    move.x += Camera.MOVE_STEP
                elif event.key == pygame.K_z:
                    move.y += -Camera.MOVE_STEP
                elif event.key == pygame.K_s:
                    move.y += Camera.MOVE_STEP
                elif event.key == pygame.K_c:
                    self.area.center = self.r_zoom.center

            # Button CLick
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse Wheel Up or Down
                if event.button == 4 or event.button == 5:
                    is_zoom_updated = True

                    if event.button == 4:
                        zoom += Camera.ZOOM_STEP
                    elif event.button == 5:
                        zoom -= Camera.ZOOM_STEP

        if is_move_updated or is_zoom_updated:
            self.__zoom(zoom)
            self.__move_area(move)

    def __zoom(self, zoom):
        # self.is_transform_updated = True
        self.r_zoom.inflate_ip(zoom, zoom)
        move = Point(zoom/2, zoom/2)
        self.__move_area(move)
        self.r_zoom.topleft = (0, 0)

        if self.r_zoom.w < self.area.w:
            self.r_zoom.w = self.area.w

        if self.r_zoom.h < self.area.h:
            self.r_zoom.h = self.area.h

    def __move_area(self, move):
        self.area.move_ip(move.x, move.y)

        if self.area.left < self.r_zoom.left:
            self.area.left = self.r_zoom.left

        if self.area.top < self.r_zoom.top:
            self.area.top = self.r_zoom.top

        if self.area.right > self.r_zoom.right:
            self.area.right = self.r_zoom.right

        if self.area.bottom > self.r_zoom.bottom:
            self.area.bottom = self.r_zoom.bottom
