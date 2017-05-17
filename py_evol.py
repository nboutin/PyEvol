import pygame

import parameters
from model import Model
from main_scene import MainScene

HD = (1280, 720)
HD_1440_900_16_10 = (1440, 900)
HD_1440_1050_4_3 = (1440, 1050)
HD_1600_1200_4_3 = (1600, 1200)
HD_1680_1050_16_10 = (1680, 1050)
FULL_HD = (1920, 1080)


def main():
    pygame.init()
    pygame.font.init()

    done = False
    clock = pygame.time.Clock()

    display_info = pygame.display.Info()
    # print (display_info)

    flags = 0 #pygame.FULLSCREEN | pygame.DOUBLEBUF
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