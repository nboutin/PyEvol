import pygame

from scene_base import SceneBase
import result_scene
import color


class MainScene(SceneBase):

    def __init__(self, rect):
        SceneBase.__init__(self)

        self.surface = pygame.Surface(rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

    def __del__(self):
        print("__del__ MainScene")

    def process_input(self, events, key_pressed):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    self.switch_to_scene(result_scene.ResultScene(self.surface.get_rect()))

                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

    def compute(self):
        pass

    def render(self, surface):
        self.surface.fill(color.LIGHT_GREEN)

        text = "Press Enter to start simulation"
        w,h = self.font.size(text)
        label = self.font.render(text, 1, color.BLACK)
        rect = self.surface.get_rect()
        self.surface.blit(label, (rect.centerx - w, rect.centery))

        surface.blit(self.surface, (0, 0))
