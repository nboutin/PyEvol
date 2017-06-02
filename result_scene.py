import pygame
import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab

from state_machine import StateMachine
from state_machine import State
from scene_base import SceneBase
import main_scene
import simulation_scene
from model import SimulationModel
from color import *


class ResultScene(SceneBase):

    WAITING_TIME = 5000  # ms
    AUTO_RUN_EVENT = pygame.USEREVENT + 1

    def __init__(self, rect, model):
        SceneBase.__init__(self)

        self.surface = pygame.Surface(rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

        self.model = model
        self.simu_model = model.simulation
        # self.on_update = True

        if self.simu_model.state == SimulationModel.State.RUNNING:
            state = Running()
        else:
            state = Populated()

        self.state_machine = StateMachineResult(state, self)

        pygame.time.set_timer(ResultScene.AUTO_RUN_EVENT, 1000)

    def switch_to_simulation(self):
        self.switch_to_scene(simulation_scene.SimulationScene(self.surface.get_rect(), self.model))

    def switch_to_main(self):
        self.switch_to_scene(main_scene.MainScene(self.surface.get_rect(), self.model))

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
        pass

    def render(self, surface):
        self.surface.fill(LIGHT_SEA_GREEN)

        label = self.font.render("Enter: Start simulation", 1, BLACK)
        self.surface.blit(label, (10, 10))

        label = self.font.render("Escape: Go to main menu", 1, BLACK)
        self.surface.blit(label, (10, 30))

        self.surface.blit(self.graph(), (100,100))

        surface.blit(self.surface, (0, 0))

    def graph(self):
        fig = pylab.figure(figsize=[4, 4], dpi=100,)
        ax = fig.gca()
        ax.plot([1, 2, 4])

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        pylab.close()

        size = canvas.get_width_height()
        return pygame.image.fromstring(raw_data, size, "RGB")


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
        sm_result.scene.simu_model.state = SimulationModel.State.POPULATED
        sm_result.scene.simu_model.construct()
        sm_result.set_state(Running())


class Evolved(StateResult):

    def on_enter(self, sm_result):
        sm_result.scene.simu_model.state = SimulationModel.State.EVOLVED
        sm_result.scene.simu_model.apply_ga()
        sm_result.set_state(Running())


class Running(StateResult):

    def on_enter(self, sm_result):
        sm_result.scene.simu_model.state = SimulationModel.State.RUNNING

    def run(self, sm_result):
        sm_result.scene.switch_to_simulation()

    def evolve(self, sm_result):
        sm_result.set_state(Evolved())

    def reset(self, sm_result):
        sm_result.set_state(Populated())

    def quit(self, sm_result):
        sm_result.set_state(Quitting())


class Waiting(StateResult):

    WAITING_TIME = 5000  # ms

    def __init__(self, next):
        self.start_time = pygame.time.get_ticks()
        self.next = next

    def ticks(self, sm_result):
        if pygame.time.get_ticks() - self.start_time >= Waiting.WAITING_TIME:
            sm_result.set_state(self.next)


class Quitting(StateResult):

    def on_enter(self, sm_result):
        sm_result.scene.simu_model.state = SimulationModel.State.QUITTING
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
