import pygame
import matplotlib
matplotlib.use("Agg")
# import matplotlib.backends.backend_agg as agg
# import pylab

from state_machine import StateMachine
from state_machine import State
from scene_base import SceneBase
import main_scene
import simulation_scene
from model import SimulationModel
from color import *


class ResultScene(SceneBase):

    WAITING_TIME = 5000  # ms

    def __init__(self, rect, model):
        SceneBase.__init__(self)

        self.surface = pygame.Surface(rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

        self.model = model
        self.simu_model = model.simulation
        # self.on_update = True

        if self.simu_model.state == SimulationModel.State.STARTED:
            state = Started()
        elif self.simu_model.state == SimulationModel.State.RUNNING:
            state = Running()

        self.state_machine = StateMachineResult(state, self)

    def switch_to_simulation(self):
        self.simu_model = SimulationModel.State.RUNNING
        self.switch_to_scene(simulation_scene.SimulationScene(self.surface.get_rect(), self.model))

    def switch_to_main(self):
        self.switch_to_scene(main_scene.MainScene(self.surface.get_rect(), self.model))
        self.simu_model = SimulationModel.State.STARTED

    def process_input(self, events, key_pressed):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Escape
                if event.key == pygame.K_ESCAPE:
                    self.state_machine.quit()
                # Enter
                elif event.key == pygame.K_RETURN:
                    pass

    def compute(self):
        pass

    def render(self, surface):
        self.surface.fill(LIGHT_SEA_GREEN)

        label = self.font.render("Enter: Start simulation", 1, BLACK)
        self.surface.blit(label, (10, 10))

        label = self.font.render("Escape: Go to main menu", 1, BLACK)
        self.surface.blit(label, (10, 30))

        surface.blit(self.surface, (0, 0))


class StateResult(State):

    def next_iteration(self, sm_result):
        pass

    def ticks(self, sm_result):
        pass

    def quit(self, sm_result):
        pass


class Started(StateResult):

    def on_enter(self, sm_result):
        sm_result.scene.simu_model.construct()
        sm_result.set_state(Running())
        sm_result.scene.switch_to_simulation()


class Running(StateResult):

    def on_enter(self, sm_result):
        sm_result.scene.simu_model.apply_ga()
        sm_result.scene.switch_to_simulation()


class Waiting(StateResult):

    WAITING_TIME = 5000  # ms

    def __init__(self, next):
        self.start_time = pygame.time.get_ticks()
        self.next = next

    def ticks(self, sm_result):
        if pygame.time.get_ticks() - self.start_time >= Waiting.WAITING_TIME:
            sm_result.set_state(self.next)


class Quiting(StateResult):

    def on_enter(self, sm_result):
        sm_result.scene.switch_to_main()


class StateMachineResult(StateMachine):

    def __init__(self, start_state, scene):
        self.scene = scene
        StateMachine.__init__(self, start_state)

    # Transition
    def next_iteration(self):
        self.current_state.launch(self)

    def ticks(self):
        self.current_state.wait(self)

    def quit(self):
        self.current_state.quit(self)
