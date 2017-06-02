import pygame
import sys
import os

import parameters
from model import Model
from main_scene import MainScene


def main():
    pygame.init()
    pygame.font.init()

    done = False
    clock = pygame.time.Clock()

    display_info = pygame.display.Info()
    print (display_info)

    icon = pygame.image.load(os.path.join("res", "icon.png"))
    pygame.display.set_icon(icon)

    flags = pygame.DOUBLEBUF | pygame.HWSURFACE
    screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), flags)
    screen.set_alpha(None)
    pygame.display.set_caption("PyEvol")

    model = Model(clock)
    active_scene = MainScene(screen.get_rect(), model)

    while not done:

        pygame.event.pump()
        key_pressed = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

        active_scene.process_input(events, key_pressed)
        active_scene.compute()
        active_scene.render(screen)
        active_scene = active_scene.next

        pygame.display.flip()

        # Limit frames per second
        model.simulation.delta_time = clock.tick(parameters.FPS)
        model.total_time_ms += model.simulation.delta_time

    pygame.quit()


if __name__ == '__main__':
    main()
    sys.exit()