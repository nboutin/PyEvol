

class State:

    def on_enter(self, state_machine):
        pass

    def on_exit(self, state_machine):
        pass


class StateMachine:

    def __init__(self, start_state):
        self.current_state = start_state

        self.current_state.on_enter(self)

    def __del__(self):
        self.current_state.on_exit(self)

    def set_state(self, state):

        self.current_state.on_exit(self)
        self.current_state = state
        self.current_state.on_enter(self)
