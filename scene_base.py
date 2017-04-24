
class SceneBase:
    def __init__(self):
        pass

    def process_input(self, events, key_pressed):
        print("uh-oh, you didn't override this in the child class")

    def compute(self):
        print("uh-oh, you didn't override this in the child class")

    def render(self, surface):
        print("uh-oh, you didn't override this in the child class")

    def terminate(self):
        pass
