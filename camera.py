import pygame


class Camera:

    (ZOOM_MIN, ZOOM_MAX, ZOOM_STEP) = (.2, 4, .2)
    MOVE_STEP = 100

    def __init__(self, rect):
        self.zoom = 1
        self.move = pygame.rect.Rect(0, 0, 1, 1)  # Size are not used here
        self.screen = rect
        self.area = rect

    def process_input(self, events):

        is_zoom_updated = False
        is_move_updated = False

        for event in events:

            # Keyboard
            if event.type == pygame.KEYDOWN:
                is_move_updated = True
                if event.key == pygame.K_q:
                    self.move.x += Camera.MOVE_STEP
                elif event.key == pygame.K_d:
                    self.move.x += -Camera.MOVE_STEP
                elif event.key == pygame.K_z:
                    self.move.y += Camera.MOVE_STEP
                elif event.key == pygame.K_s:
                    self.move.y += -Camera.MOVE_STEP

            # Button CLick
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse Wheel Up or Down
                if event.button == 4 or event.button == 5:
                    if event.button == 4:
                        self.zoom += Camera.ZOOM_STEP
                    elif event.button == 5:
                        self.zoom -= Camera.ZOOM_STEP

                    is_zoom_updated = True
                    self.zoom = clamp(self.zoom, Camera.ZOOM_MIN, Camera.ZOOM_MAX)

        # LOGIC
        if is_zoom_updated or is_move_updated:
            offset_x = -(self.screen.width * (1 - self.zoom)) / 2
            offset_y = -(self.screen.height * (1 - self.zoom)) / 2
            self.area = self.screen.inflate(offset_x, offset_y)

            self.area.move_ip(self.move.x, self.move.y)


def clamp(val, _min, _max):
    return max(min(val, _max), _min)