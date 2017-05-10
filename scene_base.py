
class SceneBase:
    def __init__(self):
        self.next = self

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def process_input(self, events, key_pressed):
        print("uh-oh, you didn't override this in the child class")

    def compute(self):
        print("uh-oh, you didn't override this in the child class")

    def render(self, surface):
        print("uh-oh, you didn't override this in the child class")

    def terminate(self):
        self.switch_to_scene(None)
