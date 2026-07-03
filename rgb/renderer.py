from rgb.controller import RGBController

class Renderer:

    def __init__(self, controller, config):

        self.rgb = controller
        self.cfg = config

    def render(self, state):

        self.rgb.set_zone(
            self.cfg["zones"]["gpu"],
            state.gpu
        )

        self.rgb.set_zone(
            self.cfg["zones"]["fans"],
            state.fans
        )
