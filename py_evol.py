import pygame

from world_scene import WorldScene
from info_scene import InfoScene


def main():
    pygame.init()
    pygame.font.init()

    screen_size = (1280, 720)
    screen_surface = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("PyEvol")

    world_view_rect = (0, 0, 800, 720)
    (world_view_width, world_view_height) = world_view_rect[2:4]
    world_view_surface = screen_surface.subsurface(world_view_rect)

    info_rect = (800, 0, 480, 720)
    info_surface = screen_surface.subsurface(info_rect)

    scenes = [(WorldScene(), world_view_surface),
              (InfoScene(), info_surface)]

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for (scene, surface) in scenes:

            # scene.process_input()
            scene.compute()
            scene.render(surface)

        pygame.display.flip()

        # Limit frames per second
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()