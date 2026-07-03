import time

from rgb.controller import RGBController
from rgb.renderer import Renderer
from rgb.animator import Animator
from rgb.theme import ThemeLoader

from config import Config

cfg = Config()

controller = RGBController()

renderer = Renderer(controller, cfg)

animator = Animator()

loader = ThemeLoader()

current = loader.load("sakura")
target = loader.load("crimson")

animator.start(current, target, 120)

while True:

    state = animator.update()

    renderer.render(state)

    time.sleep(1/30)
