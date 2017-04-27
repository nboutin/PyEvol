import pygame

from world_scene import WorldScene
from info_scene import InfoScene


HD = (1280, 720)

HD_1440_900_16_10 = (1440, 900)
HD_1440_1050_4_3 = (1440, 1050)

HD_1600_1200_4_3 = (1600, 1200)
HD_1680_1050_16_10 = (1680, 1050)

FULL_HD = (1920, 1080)


def main():
    pygame.init()
    pygame.font.init()

    screen_size = HD_1440_1050_4_3
    screen_surface = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("PyEvol")

    world_view_rect = (0, 0, screen_size[1], screen_size[1])
    (world_view_width, world_view_height) = world_view_rect[2:4]
    world_view_surface = screen_surface.subsurface(world_view_rect)

    info_rect = (screen_size[1], 0, screen_size[0] - screen_size[1], screen_size[1])
    info_surface = screen_surface.subsurface(info_rect)

    world_scene  = WorldScene()
    info_scene = InfoScene(world_scene)
    scenes = [(world_scene, world_view_surface),
              (info_scene, info_surface)]

    done = False
    clock = pygame.time.Clock()

    while not done:

        pygame.event.pump()
        key_pressed = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True

        for (scene, surface ) in scenes:
            scene.process_input(events, key_pressed)

        for (scene, surface) in scenes:
            scene.compute()
            scene.render(surface)

        pygame.display.flip()

        # Limit frames per second
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()