import pygame
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg

# import pylab

from state_machine import StateMachine
from state_machine import State
from scene_base import SceneBase
import main_scene
import simulation_scene
from model import model
from model import simulation_model
from model import SimulationModel
SimState = SimulationModel.State
from color import *


class ResultScene(SceneBase):
    WAITING_TIME = 5000  # ms
    AUTO_RUN_EVENT = pygame.USEREVENT + 1

    def __init__(self, rect):
        SceneBase.__init__(self)

        self.surface = pygame.Surface(rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

        if simulation_model.state == SimState.RUNNING:
            state = Running()
        else:
            state = Populated()

        self.state_machine = StateMachineResult(state, self)

        # Graph
        self.graph_surface = None
        self.fig = plt.figure(figsize=[6, 6], dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = agg.FigureCanvasAgg(self.fig)

        pygame.time.set_timer(ResultScene.AUTO_RUN_EVENT, 3000)

    # def __del__(self):
    def on_exit(self):
        print("on_exit ResultScene")
        plt.close(self.fig)
        print(plt.get_fignums())

    def switch_to_simulation(self):
        self.switch_to_scene(simulation_scene.SimulationScene(self.surface.get_rect()))

    def switch_to_main(self):
        self.switch_to_scene(main_scene.MainScene(self.surface.get_rect()))

    def process_input(self, events, key_pressed):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Escape
                if event.key == pygame.K_ESCAPE:
                    self.state_machine.quit()
                # Enter
                elif event.key == pygame.K_RETURN:
                    self.state_machine.run()
                # e
                elif event.key == pygame.K_e:
                    self.state_machine.evolve()
                # r
                elif event.key == pygame.K_r:
                    self.state_machine.reset()

            elif event.type == ResultScene.AUTO_RUN_EVENT:
                self.state_machine.evolve()
                self.state_machine.run()
                pygame.time.set_timer(ResultScene.AUTO_RUN_EVENT, 0)  # stop timer

    def compute(self):

        if not self.graph_surface:
            self.graph_surface = self.plot(simulation_model.stat.maximums)

    def render(self, surface):
        self.surface.fill(LIGHT_SEA_GREEN)

        label = self.font.render("Enter: Start simulation", 1, BLACK)
        self.surface.blit(label, (10, 10))

        label = self.font.render("Escape: Go to main menu", 1, BLACK)
        self.surface.blit(label, (10, 30))

        self.surface.blit(self.graph_surface, (100, 100))

        surface.blit(self.surface, (0, 0))

    def plot(self, data):
        self.ax.plot(data)
        self.canvas.draw()
        renderer = self.canvas.get_renderer()

        raw_data = renderer.tostring_rgb()
        size = self.canvas.get_width_height()

        return pygame.image.fromstring(raw_data, size, "RGB")

        # def graph(self):
        #
        #     if not self.graph_surface:
        #
        #         fig = plt.figure(figsize=[3, 3])
        #         ax = fig.add_subplot(111)
        #         canvas = agg.FigureCanvasAgg(fig)
        #
        #
        #         # fig = pylab.figure(figsize=[6, 6], dpi=100,)
        #         # ax = fig.gca()
        #         # ax.plot([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        #         # # ax.plot(self.simu_model.stat.maximums)
        #         #
        #         # self.graph_surface = self.make_fig2(fig)
        #
        #         # plt.plot([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        #         # plt.plot(self.simu_model.stat.maximums)
        #         # canvas = plt.get_current_fig_manager().canvas
        #         #
        #         # agg = canvas.switch_backends(FigureCanvasAgg)
        #         # agg.draw()
        #         # raw_data = agg.tostring_rgb()
        #         #
        #         # l, b, w, h = agg.figure.bbox.bounds
        #         # w, h = int(w), int(h)
        #         # self.graph_surface = pygame.image.fromstring(raw_data, (w, h), "RGB")
        #
        #     return self.graph_surface


        # @staticmethod
        # def make_fig2(fig):
        #     canvas = plt.get_current_fig_manager().canvas
        #     canvas.draw()
        #     renderer = canvas.get_renderer()
        #     raw_data = renderer.tostring_rgb()
        #     pylab.close(fig)
        #
        #     size = canvas.get_width_height()
        #     return pygame.image.fromstring(raw_data, size, "RGB")


        # @staticmethod
        # def make_fig(fig):
        #     canvas = agg.FigureCanvasAgg(fig)
        #     canvas.draw()
        #     renderer = canvas.get_renderer()
        #     raw_data = renderer.tostring_rgb()
        #     pylab.close(fig)
        #
        #     size = canvas.get_width_height()
        #     return pygame.image.fromstring(raw_data, size, "RGB")


class StateResult(State):
    def evolve(self, sm_result):
        pass

    def run(self, sm_result):
        pass

    def ticks(self, sm_result):
        pass

    def reset(self, sm_result):
        pass

    def quit(self, sm_result):
        pass


class Populated(StateResult):
    def on_enter(self, sm_result):
        simulation_model.state = SimState.POPULATED
        simulation_model.construct()
        sm_result.set_state(Running())


class Evolved(StateResult):
    def on_enter(self, sm_result):
        simulation_model.state = SimState.EVOLVED
        simulation_model.prepare_next_iteration()
        sm_result.set_state(Running())


class Running(StateResult):
    def on_enter(self, sm_result):
        simulation_model.state = SimState.RUNNING

    def run(self, sm_result):
        sm_result.scene.switch_to_simulation()

    def evolve(self, sm_result):
        sm_result.set_state(Evolved())

    def reset(self, sm_result):
        sm_result.set_state(Populated())

    def quit(self, sm_result):
        sm_result.set_state(Quitting())


# class Waiting(StateResult):
#     WAITING_TIME = 5000  # ms
#
#     def __init__(self, next):
#         self.start_time = pygame.time.get_ticks()
#         self.next = next
#
#     def ticks(self, sm_result):
#         if pygame.time.get_ticks() - self.start_time >= Waiting.WAITING_TIME:
#             sm_result.set_state(self.next)


class Quitting(StateResult):
    def on_enter(self, sm_result):
        simulation_model.state = SimState.QUITTING
        sm_result.scene.switch_to_main()


class StateMachineResult(StateMachine):
    def __init__(self, start_state, scene):
        self.scene = scene
        StateMachine.__init__(self, start_state)

    # Transition
    def evolve(self):
        self.current_state.evolve(self)

    def run(self):
        self.current_state.run(self)

    def ticks(self):
        self.current_state.wait(self)

    def reset(self):
        self.current_state.reset(self)

    def quit(self):
        self.current_state.quit(self)
